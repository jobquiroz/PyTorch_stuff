import shutil
from tensorboard import manager

def tensorboard_cleanup():
    info_dir = manager._get_info_dir()
    shutil.rmtree(info_dir)

FOLDERS = {
    0: ['plots'],
    1: ['plots'],
    2: ['plots', 'data_generation', 'data_preparation', 'model_configuration', 'model_training'],
    21: ['plots', 'data_generation', 'data_preparation', 'model_configuration', 'stepbystep'],
    3: ['plots', 'stepbystep'],
    4: ['plots', 'stepbystep', 'data_generation'],
    5: ['plots', 'stepbystep', 'data_generation', ''],
    6: ['plots', 'stepbystep', 'stepbystep', 'data_generation', 'data_generation', 'data_preparation'],
    7: ['plots', 'stepbystep', 'data_generation'],
    71: ['plots', 'stepbystep', 'data_generation'],
    8: ['plots', 'plots', 'stepbystep', 'data_generation'],
    9: ['plots', 'plots', 'plots', 'stepbystep', 'data_generation'],
    10: ['plots', 'plots', 'plots', 'plots', 'stepbystep', 'data_generation', 'data_generation', '', ''],
    11: ['plots', 'stepbystep', 'data_generation', ''],
}
FILENAMES = {
    0: ['chapter0.py'],
    1: ['chapter1.py'],
    2: ['chapter2.py', 'simple_linear_regression.py', 'v0.py', 'v0.py', 'v0.py'],
    21: ['chapter2_1.py', 'simple_linear_regression.py', 'v2.py', '', 'v0.py'],
    3: ['chapter3.py', 'v0.py'],
    4: ['chapter4.py', 'v0.py', 'image_classification.py'],
    5: ['chapter5.py', 'v1.py', 'image_classification.py', 'helpers.py'],
    6: ['chapter6.py', 'v2.py', 'v3.py', 'rps.py', 'simple_linear_regression.py', 'v2.py'],
    7: ['chapter7.py', 'v3.py', 'rps.py'],
    71: ['chapterextra.py', 'v3.py', 'ball.py'],
    8: ['chapter8.py', 'replay.py', 'v4.py', 'square_sequences.py'],
    9: ['chapter8.py', 'chapter9.py', 'replay.py', 'v4.py', 'square_sequences.py'],
    10: ['chapter8.py', 'chapter9.py', 'chapter10.py', 'replay.py', 'v4.py', 'square_sequences.py', 'image_classification.py', 'helpers.py', 'seq2seq.py'],
    11: ['chapter11.py', 'v4.py', 'nlp.py', 'seq2seq.py'],
}
