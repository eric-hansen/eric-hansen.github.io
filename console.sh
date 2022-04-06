#!/bin/bash

CMD="$1"

shift

_hugo_cmd () {
    hugo -s site --themesDir=../themes "$@"
}

hugo_new_post () {
    FOLDER_TS=$(date +%Y/%m)
    FILE_PARTS="$@"
    echo "> Filename given: $FILE_PARTS"
    FILE=${FILE_PARTS//[_ ]/-}
    echo "> Converted filename: $FILE"

    mkdir -p site/content/posts/$FOLDER_TS

    _hugo_cmd -k posts posts/$FOLDER_TS/$FILE.md
}

hugo_serve () {
    _hugo_cmd serve
}

case "$CMD" in
    new_post)
    hugo_new_post "$@"
    ;;
    serve)
    hugo_serve "$@"
    ;;
    *)
    echo "Unknown command: $CMD"
    exit 1
    ;;
esac

exit 0