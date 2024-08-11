from io import BytesIO
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://ieee-dataport.s3.amazonaws.com/open/54588/allDataMean.csv?response-content-disposition=attachment%3B%20filename%3D%22allDataMean.csv%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJOHYI4KJCE6Q7MIQ%2F20240724%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240724T050721Z&X-Amz-SignedHeaders=Host&X-Amz-Expires=86400&X-Amz-Signature=945fb008dd998b1bbf1d9b14f508167b7100ce5832131ea0a0bda52e64e23aa1'

    response = requests.get(url, stream=True)

    # with open('descargado.csv', 'wb') as fd:
    #     for chunk in response.iter_content(chunk_size=20000):
    #         fd.write(chunk)

    # chunksize = 10 ** 6  # Define el tamaño del chunk en número de filas
    # chunks = []

    # for chunk in pd.read_csv('descargado.csv', chunksize=chunksize):
    #     # Procesa cada chunk aquí si es necesario
    #     chunks.append(chunk)

    # Opcionalmente, puedes concatenar todos los chunks en un solo DataFrame si tu memoria lo permite
    # df = pd.concat(chunks, axis=0)


    df = pd.read_csv(BytesIO(response.content))
            # dfs.append(df)

    return df.head(15)


