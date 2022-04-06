#!/bin/bash

CMD="$1"

shift

hugo_new_post () {
    FOLDER_TS=$(date +%Y/%m)
    FILE_PARTS="$@"
    echo "> Filename given: $FILE_PARTS"
    FILE=${FILE_PARTS//[_ ]/-}
    echo "> Converted filename: $FILE"

    mkdir -p site/content/posts/$FOLDER_TS

    hugo new -s site -k posts --themesDir=../themes posts/$FOLDER_TS/$FILE.md
}

case "$CMD" in
    new_post)
    hugo_new_post "$@"
    ;;

    *)
    echo "Unknown command: $CMD"
    exit 1
    ;;
esac

exit 0