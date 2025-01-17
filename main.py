from cnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from cnnClassifier.pipeline.stage_05_callbacks import CallbacksPipeline


STAGE_NAME = "Data Ingestion stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)


STAGE_NAME = "Prepare base model"
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)


STAGE_NAME = "Training"
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)


STAGE_NAME = "Evaluation stage"
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        model_evalution = EvaluationPipeline()
        model_evalution.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)


STAGE_NAME = "CallBacks stage"
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        callbacks_action = CallbacksPipeline()
        callbacks_action.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
