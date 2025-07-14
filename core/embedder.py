from core.trt_engine import TrtEngine

class FaceEmbedder:
    def __init__(self, engine_path):
        self.engine = TrtEngine(engine_path)

    def embed(self, aligned_face):
        # Extract embedding
        pass
