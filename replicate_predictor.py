from contextlib import suppress
from min_dalle import MinDalle
import tempfile
from typing import Iterator
from math import log2
from cog import BasePredictor, Path, Input


class ReplicatePredictor(BasePredictor):
    def setup(self):
        self.model = MinDalle(is_mega=True)

    def predict(
        self,
        text: str = Input(
            description='Text',
            default='Dali painting of WALL·E'
        ),
        grid_size: int = Input(
            description='Size of the image grid',
            ge=1,
            le=4,
            default=4
        ),
        seed: int = Input(
            description='Set the seed to a positive number for reproducible results',
            default=-1
        ),
        log2_intermediate_image_count: int = Input(
            description='Set the number of intermediate images to show while running',
            ge=0,
            le=4,
            default=2
        ),
        log2_supercondition_factor: int = Input(
            description='Lower results in a wider variety of images but less agreement with the text',
            ge=1,
            le=6,
            default=4
        ),
    ) -> Iterator[Path]:
        image_stream = self.model.generate_image_stream(
            text,
            seed,
            grid_size=grid_size,
            log2_mid_count=log2_intermediate_image_count,
            log2_supercondition_factor=log2_supercondition_factor,
            is_verbose=True
        )

        iter = 0
        path = Path(tempfile.mkdtemp())
        for image in image_stream:
            iter += 1
            image_path = path / 'min-dalle-iter-{}.jpg'.format(iter)
            image.save(str(image_path))
            yield image_path