#!/usr/bin/env python3

import connexion

from jobbing import encoder

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Aprende tu mismo API'}, pythonic_params=True)


if __name__ == '__main__':
    app.run()
