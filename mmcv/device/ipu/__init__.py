# Copyright (c) OpenMMLab. All rights reserved.
from .utils import IPU_MODE


if IPU_MODE:
    from .model_wrapper import (parse_ipu_options, ipu_model_wrapper,
                                build_from_cfg_with_wrapper, model_sharding,
                                recomputation_checkpoint)
    from .hook_wrapper import (wrap_optimizer_hook, IPUFp16OptimizerHook,
                               wrap_lr_updater_hook)
    from .dataloader import IPUDataLoader
    from .runner import IPUBaseRunner, IPUEpochBasedRunner, IPUIterBasedRunner
    __all__ = [
        'parse_ipu_options', 'ipu_model_wrapper',
        'build_from_cfg_with_wrapper', 'IPU_MODE',
        'model_sharding', 'wrap_optimizer_hook',
        'IPUFp16OptimizerHook', 'wrap_lr_updater_hook',
        'recomputation_checkpoint', 'IPUDataLoader',
        'IPUBaseRunner', 'IPUEpochBasedRunner',
        'IPUIterBasedRunner'
    ]
