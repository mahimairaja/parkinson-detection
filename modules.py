from super_gradients.training import models
import supervision as sv
import torch
import cv2

# install the required packages
# pip install -q super-gradients==3.1.1 supervision

# predict function to predict the image
def predict(img, model):
    """
        Predict the image and return the annotated image and labels.
    """
    SOURCE_IMAGE_PATH = img
    image = cv2.imread(SOURCE_IMAGE_PATH)
    result = list(model.predict(image, conf=0.70))[0]
    # Create detections object
    detections = sv.Detections(
        xyxy=result.prediction.bboxes_xyxy,
        confidence=result.prediction.confidence,
        class_id=result.prediction.labels.astype(int)
    )
    # Create a box annotator
    box_annotator = sv.BoxAnnotator()
    # Get the labels
    labels = [
        f"{result.class_names[class_id]} {confidence:0.2f}"
        for _, _, confidence, class_id, _
        in detections
    ]
    # Annotate the image
    annotated_frame = box_annotator.annotate(
        scene=image.copy(),
        detections=detections,
        labels=labels
    )

    # sv.plot_image(annotated_frame, (12, 12))
    return annotated_frame, labels


def setup():
    """
        Setup the model and return it.
    """
    DEVICE = 'cuda' if torch.cuda.is_available() else "cpu" # 'cpu' or 'cuda'
    MODEL_ARCH = 'yolo_nas_l'

    # Load the model
    model = models.get( 
        MODEL_ARCH,
        num_classes=2,
        checkpoint_path="model.pth"
    ).to(DEVICE)
    return model