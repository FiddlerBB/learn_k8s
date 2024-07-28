# Define the image name
IMAGE=fiddlerbb/scrape_book

# Default target
all: build push

# Build the Docker image
build:
	docker build -t ${IMAGE}:latest -f Dockerfile .

run:
	docker run --rm -it -v $(pwd)/src/out:/out ${IMAGE}

# Push the Docker image
push:
	docker push ${IMAGE}:latest

create:
	kubectl apply -f deploy.yml