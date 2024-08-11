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


    df = pd.read_csv(BytesIO(response.content))
            # dfs.append(df)

    return df.head(15)

