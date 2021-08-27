# python imports
import json
import boto3
from io import BytesIO
import py7zlib

def lambda_handler(event, context):
    

    # Configuração 
    bucket = '<bucket-name>'
    gzipped_key = '<keyfile.7z>'
    uncompressed_key = '<keyfile.txt>'
    
    
    
    # initialize s3 client, this is dependent upon your aws config being done 
    s3 = boto3.client('s3', use_ssl=False)  
    fileobj=BytesIO(s3.get_object(Bucket=bucket, Key=gzipped_key)['Body'].read())
    archive = py7zlib.Archive7z(fileobj)
    
    
    
    # BytesIO é necessário novamente porque quando tentamos utilizar FileObj temos:
    # ---- "TypeError: method() takes 1 positional argument but 2 were given"
    data = BytesIO(archive.getmember(archive.getnames()[0]).read()) 
    
    
    # Upload
    s3.upload_fileobj(                      
           Fileobj=data,
           Bucket=bucket,                      
           Key=uncompressed_key               
    )     
    
    return {
        'statusCode': 200,
        'body': json.dumps('Arquivo txt gravado com sucesso.')
    }
