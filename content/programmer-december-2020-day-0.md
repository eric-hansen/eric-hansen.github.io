Title: Programmer December 2020 - Day 0
Slug: programmer-december-2020-day-0
Date: 2020-11-29


This year's adventure is going to be interesting as we explore challenges through [Daily Coding Problem](https://www.dailycodingproblem.com/).  As this is something I've never done before (just signed up for these guys today actually), I figured I would spend a Sunday hacking away for a little bit on their problem they just emailed me:

```
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
```

These blog entries will be to show my thinking process and workflow through these problems.  I can't guarantee I'll blog every challenge but will do what I can.

### Known
I like to start off by listing things that are known (constraints) and unknown, if possible.

Here we have a few things we know off the bat:
* Working with arrays of integers (we'll call this A)
* K = sum of any pairs of numbers within A
* Returns true if any pairs of A[n] + A[o] = K, else false
* sizeof(A) >= 2, otherwise we cannot check the formula above

### Language Choice & Why
For this I'll solve this in PHP.  It's the language I'm most familiar with and can explain the best.  I'm not going to count this against my "use the language only once" for my challenge.

### Step 1: Framework
Here we need a good foundation to solve this problem.  Everything is pretty simple here (and is ranked as "easy" by DPC).

```php
<?php
$a = explode(",", $argv[1]);
$k = $argv[2];

echo "Checking array of [" . implode(", ", $a) . "] for sum of " . $k . "\n";
?>
```

So this is what we'll start off with.  So how this script will work is like so:

```
erich@DESKTOP-HE7V7MB ~/Projects/programmer-december/0
 % php challenge.php 10,15,3,7 17
Checking array of [10, 15, 3, 7] for sum of 17
```

### Step 2: Come up with all possible options
This is definitely not going to be a performance-friendly option, but it at least solves the test data effectively.

```php
<?php
...
$pairs = [];

foreach ($a as $pos => $val) {
  foreach ($a as $subPos => $subVal) {
    if ($subPos != $pos) {
       if (!isset($pairs[$val])) $pairs[$val] = [];
        $pairs[$val][] = $subVal;
    }
  }
}
...
?>
```

We want to get all possible pairs from A[n],A[x] ignoring itself. Which is probably easier to explain visually:

```
array(4) {
  [10]=>
  array(3) {
    [0]=>
    string(2) "15"
    [1]=>
    string(1) "3"
    [2]=>
    string(1) "7"
  }
  [15]=>
  array(3) {
    [0]=>
    string(2) "10"
    [1]=>
    string(1) "3"
    [2]=>
    string(1) "7"
  }
  [3]=>
  array(3) {
    [0]=>
    string(2) "10"
    [1]=>
    string(2) "15"
    [2]=>
    string(1) "7"
  }
  [7]=>
  array(3) {
    [0]=>
    string(2) "10"
    [1]=>
    string(2) "15"
    [2]=>
    string(1) "3"
  }
}
```

So each root element of `$pairs` will be the starting (A[n]) and that holds an array of possible values for A[x].

Now, we can either make this simple (which I'll show here), or we can carry this a bit further which I'll demonstrate second.

### Step 3: Simple Solution
Here's the simple solution:

```php
<?php
...
$found = false;

foreach ($a as $pos => $val) {
  foreach ($a as $subPos => $subVal) {
    if (($val + $subVal) == $k) {
      $found = true;
      break;
    }
  }
}

echo("Found a pair that sums to " . $k . "? " . ($found ? "Yes" : "No") . "\n");
...
?>
```

Instead of cycling through all possible options we just need to know if one match is found.  If so, lets inform the runner.

This is pretty simple.  Now for the over engineered one!

### Step 4: Over-Engineered Solution
Not too different than the above, it's just moving some logic around primarily:

```php
<?php
...
foreach ($a as $pos => $val) {
  foreach ($a as $subPos => $subVal) {
       if (!isset($pairs[$val])) $pairs[$val] = [];
        $pairs[$val][] = $subVal;
  }
}

array_walk($pairs, function ($subVals, $val) use (&$found, $k) {
  if ($found) return;

  foreach ($subVals as $subVal) {
    if (($val + $subVal) == $k) {
      $found = true;
      break;
    }
  }
});
...
?>
```
Here we use `array_walk` to step through the `$pairs` array, then create a lambda/closure to finish processing all the values.

Both solutions warran the exected outcome:

```
erich@DESKTOP-HE7V7MB ~/Projects/programmer-december/0
 % php challenge.php 10,15,3,7 17
Checking array of [10, 15, 3, 7] for sum of 17
Found a pair that sums to 17? Yes
```