# Sprocket Factory API

## Setup

1. Clone the repository.
2. Create a virtual environment.
3. Install the dependencies with `pip install -r requirements.txt`.
4. Run the API with `python main.py`.

## Endpoints

### GET /factories

Returns all sprocket factory data.

### GET /factories/<id>

Returns factory data for the given factory id.

### GET /sprockets/<id>

Returns sprockets data for the given sprocket id.

### POST /sprockets

Creates a new sprocket. 

### PUT /sprockets/<id>

Updates the sprocket for the given sprocket id.