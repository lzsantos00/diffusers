# Copyright 2024 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from ..utils import (
    DIFFUSERS_SLOW_IMPORT,
    _LazyModule,
    is_accelerate_available,
    is_bitsandbytes_available,
    is_torch_available,
)


_import_structure = {}

if is_torch_available():
    _import_structure["base"] = ["DiffusersQuantizer"]
    if is_bitsandbytes_available() and is_accelerate_available():
        _import_structure["bitsandbytes"] = [
            "set_module_quantized_tensor_to_device",
            "replace_with_bnb_linear",
            "dequantize_bnb_weight",
            "dequantize_and_replace",
        ]

if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:
    if is_torch_available():
        from .base import DiffusersQuantizer

        if is_bitsandbytes_available() and is_accelerate_available():
            from .bitsandbytes import (
                dequantize_and_replace,
                dequantize_bnb_weight,
                replace_with_bnb_linear,
                set_module_quantized_tensor_to_device,
            )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)