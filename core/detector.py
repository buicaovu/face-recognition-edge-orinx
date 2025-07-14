from core.trt_engine import TrtEngine

class FaceDetector:
    def __init__(self, engine_path, input_shape):
        self.engine = TrtEngine(engine_path)
        self.input_shape = input_shape

    def detect(self, frame):
        # Preprocess, run inference, postprocess detections
        pass
