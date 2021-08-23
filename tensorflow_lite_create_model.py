"""
https://github.com/yoeo/guesslang/issues/26
https://www.tensorflow.org/guide/saved_model
https://www.tensorflow.org/lite/convert
"""
from tempfile import TemporaryDirectory

import tensorflow as tf
from guesslang import Guess

guess = Guess()

saved_model_dir = TemporaryDirectory()
tf.saved_model.save(guess._model, saved_model_dir.name)

# guess._model.signatures
# _SignatureMap({'classification': <ConcreteFunction pruned(inputs) at 0x16759F130>,
#                'serving_default': <ConcreteFunction pruned(inputs) at 0x167628790>,
#                'predict': <ConcreteFunction pruned(content) at 0x167677B20>})

if False:
    # Try to convert a "saved model"
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir.name)
    # Traceback (most recent call last):
    # File "/Users/dan/src/misc-python/tensorflow_lite_create_model.py", line 13, in <module>
    #     converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir.name)
    # File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/lite/python/lite.py", line 1275, in from_saved_model
    #     raise ValueError("Only support a single signature key.")
    # ValueError: Only support a single signature key.

if True:
    # Try to convert a "saved model", passing signature_keys
    converter = tf.lite.TFLiteConverter.from_saved_model(
        saved_model_dir.name, signature_keys=["predict"]
    )
    # Traceback (most recent call last):
    #   File "/Users/dan/src/misc-python/tensorflow_lite_create_model.py", line 28, in <module>
    #     converter = tf.lite.TFLiteConverter.from_saved_model(
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/lite/python/lite.py", line 1280, in from_saved_model
    #     raise ValueError("Invalid signature key '{}' found. Valid keys are "
    # ValueError: Invalid signature key 'predict' found. Valid keys are ''.


if False:
    # Try to convert "concrete function"
    concrete_fn = guess._model.signatures["predict"]
    converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_fn])
    tflite_model = converter.convert()
    # Traceback (most recent call last):
    #   File "/Users/dan/src/misc-python/tensorflow_lite_create_model.py", line 17, in <module>
    #     tflite_model = converter.convert()
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/lite/python/lite.py", line 1318, in convert
    #     return super(TFLiteConverterV2, self).convert()
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/lite/python/lite.py", line 1108, in convert
    #     _convert_to_constants.convert_variables_to_constants_v2_as_graph(
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/framework/convert_to_constants.py", line 1109, in convert_variables_to_constants_v2_as_graph
    #     converter_data = _FunctionConverterData(
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/framework/convert_to_constants.py", line 801, in __init__
    #     graph_def = _run_inline_graph_optimization(func, lower_control_flow,
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/framework/convert_to_constants.py", line 973, in _run_inline_graph_optimization
    #     return tf_optimizer.OptimizeGraph(config, meta_graph)
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/grappler/tf_optimizer.py", line 55, in OptimizeGraph
    #     out_graph = tf_opt.TF_OptimizeGraph(cluster.tf_cluster,
    # ValueError: Failed to import metagraph, check error log for more info.


if False:
    concrete_fn = guess._model.signatures["classification"]
    converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_fn])
    tflite_model = converter.convert()
    # Traceback (most recent call last):
    #   File "/Users/dan/src/misc-python/tensorflow_lite_create_model.py", line 41, in <module>
    #     tflite_model = converter.convert()
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/lite/python/lite.py", line 1318, in convert
    #     return super(TFLiteConverterV2, self).convert()
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/lite/python/lite.py", line 1108, in convert
    #     _convert_to_constants.convert_variables_to_constants_v2_as_graph(
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/framework/convert_to_constants.py", line 1109, in convert_variables_to_constants_v2_as_graph
    #     converter_data = _FunctionConverterData(
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/framework/convert_to_constants.py", line 801, in __init__
    #     graph_def = _run_inline_graph_optimization(func, lower_control_flow,
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/framework/convert_to_constants.py", line 973, in _run_inline_graph_optimization
    #     return tf_optimizer.OptimizeGraph(config, meta_graph)
    #   File "/Users/dan/.pyenv/versions/3.9.1/lib/python3.9/site-packages/tensorflow/python/grappler/tf_optimizer.py", line 55, in OptimizeGraph
    #     out_graph = tf_opt.TF_OptimizeGraph(cluster.tf_cluster,
    # ValueError: Failed to import metagraph, check error log for more info.
