from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
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
        
        data_transformation_config=DataTransformationConfig(TrainingPipelineconfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")


        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(TrainingPipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()


    except Exception as e:
        raise NetworkSecurityException(e,sys)
