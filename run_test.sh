docker build . --tag "pythonbq" --quiet
docker run -it --rm \
    --volume "$(pwd):/app" \
    "pythonbq"

