from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys 

if __name__== "__main__":
    try:
        TrainingPipelineconfig = TrainingPipelineConfig()   
        print("trainingpipeline done")
        dataingestionconfig = DataIngestionConfig(TrainingPipelineconfig)
        print("dataingestion training done")
        dataingestion= DataIngestion(dataingestionconfig)
        print("dataingestion done")
        logging.info("Initiate the data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print("dataingestionartifact done")
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
