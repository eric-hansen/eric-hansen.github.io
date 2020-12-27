Title: Programmer December 2020 - Day 1
Slug: programmer-december-2020-day-1
Date: 2020-12-01


Today's challenge is an interesting one and it's ranked hard.  Lets see what the challenge itself is...

```
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
```

This has an additional yet optional task but as it gives away the answer for the challenge for easiest path, I'm not going to disclose it just yet, if at all. :)

### Known Constraints
Here we have a few things we know off the bat:
* We will be working with arrays of integers (`int[]`), called A
* Our function will return a new array (meaning no manging A), called B
* `B[x] = sum(product(A[0...n (excluding x)]))`
* size(A) == size(B)

### Language Choice & Why
I was thinking of doing this in Shell, but I really am not a fan of working with arrays in that.  Instead I will do this in Lua.  Partially because I've been rewriting my Neovim config in Lua and also because it's a fun functional language.

### Step 1: Framework
We know we will have an array of integers and the function will create a new array from that set.  So we will start from there:

```lua
function main(intArray)
  local newArray = {}

  return newArray
end
```

In Lua, unlike other languages like PHP, JS, etc... arrays are defined as `{}` instead of `[]`.

### Step 2: Cycle Through intArray

We want to cycle through all the values of `intArray` to ensure we can get each value.  As I am far from experienced in Lua, don't laugh (and this goes for the other days too lol) at my inefficient routines.  I may revise these later after this challenge is over.

I created a second function to do this for me (though itself could have just been a lambda):

```lua
function iterateArray(array, positionToIgnore, lambda)
  for index, val in ipairs(array) do
    if (index ~= positionToIgnore) then lambda(val) end
  end
end
```

No error checking in any of this because I just want to get a proof of concept going.

We loop through the key-value pairs of the array (which is just a table/dictionary) and if the current position isn't the position we ant to ignore we call the callable to process the value.

When I first wrote this I wasn't sure if what I did even would work by a long shot...

### Step 3: Modify main() function

Now we need to plug this new `iterateArray` function into our main function and process data.  My config for Neovim makes use of lambdas a bit so that's why I'm doing it this way:

```lua
function main(intArrays)
  local newArray = {}

  for i, v in ipairs(intArrays) do
    prod = 1
    iterateArray(intArrays, i, function(val) prod = prod * val end)
    newArray[i] = prod
  end

  return newArray
end
```

We again loop and then we call our new function.  We define `prod = 1` at the beginning of each loop because we need some truthy value in the lambda and if `val` is ever 0 then it'll 0-out `prod` anyways.

The lamba, in theory, will assign a new value to `prod` based on each value processed.  In PHP we would have to write this as 
```php
<?php
function ($val) use (&$prod) { ... }
?>
```
My fear is that `prod` won't be updated given my PHP conditioning I have.

### Step 4: Print Out Results

Before I finalized running this I wanted to spit stuff out on the console.  I tried `print(main({...}))` (filling `...` with actual values) but it just printed a reference to the table (i.e.: `table: 0x55b3cda506f0`).  Obviously not very helpful.  So after browsing the web and not wanting to add additional packages besides what's standard, I found this gem: ```print(table.concat(main({3, 2, 1}), ", "))``` which is basically just a `join(", ", main([3, 2, 1]))` in PHP-land.

### Step 5: Full Result & Output
Here's the finalized code I have:

```lua
function iterateArray(array, positionToIgnore, lambda)
  for index, val in ipairs(array) do
    if (index ~= positionToIgnore) then lambda(val) end
  end
end

function main(intArrays)
  local newArray = {}

  for i, v in ipairs(intArrays) do
    prod = 1
    iterateArray(intArrays, i, function(val) prod = prod * val end)
    newArray[i] = prod
  end

  return newArray
end

print(table.concat(main({3, 2, 1}), ", "))
```

The output for this is:

```
erich@DESKTOP-HE7V7MB ~/Projects/programmer-december/1
 % lua challenge.lua
2, 3, 6
```

Which matches the expected result.  As for the second data provided:

```
erich@DESKTOP-HE7V7MB ~/Projects/programmer-december/1
 % lua challenge.lua
120, 60, 40, 30, 24
```

### Step 6: Thoughts
I realized at the end I never did the division solution to begin with.  That would've been far easier in theory, because you just need to aggregate-sum the product of each element and then divide the current value by that sum.

As an example with the `3, 2, 1` data set:

```
A[0] = 3, A[1] = 2, A[2] = 1
S = ((2 * 1) + (3 * 1) + (2 * 3)) = 9
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