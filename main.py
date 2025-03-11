from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
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
        #print(dataingestionartifact)

        data_validation_config = DataValidationConfig(TrainingPipelineconfig)
        print("started data validation")
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")   
        print("data validation initiated") 
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")   
        print("data validation completed")
        print(data_validation_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
