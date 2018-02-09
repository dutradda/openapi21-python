from openapi21 import validate_spec, validate_spec_url

spec = {
    "swagger":"2.1",
    "info":{
        "version": "0.0.1",
        "title": "Store Example"
    },
    "paths": {
        "allOf": [{
            "$ref": "dresses/swagger.json"
        },{
            "$ref": "shoes/swagger.json"
        }]
    },
    "definitions": {
        "allOf": [{
            "$ref": "definitions.json"
        },{
            "$ref": "dresses/definitions.json"
        },{
            "$ref": "shoes/definitions.json"
        }]
    }
}

validate_spec(spec, spec_url='OpenAPI-Specification-2.1'
                             '/example/swagger.json')

validate_spec_url('http://cdn.rawgit.com/dutradda/'
                  'OpenAPI-Specification-2.1/master'
                  '/example/swagger.json')
