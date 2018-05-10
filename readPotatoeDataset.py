import numpy as np
import os
import glob
from IPython import embed

def read_dataset(tatersDir):
    
    testImagesLocation = os.path.join(tatersDir, "test")
    testAnotationsLocation = os.path.join(tatersDir, "test_labels")
    trainImagesLocation = os.path.join(tatersDir, "train")
    trainAnotationsLocation = os.path.join(tatersDir, "train_labels")

    '''
    training_records should be a list of objects with this format:
    {'annotation': 'Data_zoo/MIT_SceneParsing/ADEChallengeData2016/annotations/training/ADE_train_00013892.png',
      'filename': 'ADE_train_00013892',
      'image': 'Data_zoo/MIT_SceneParsing/ADEChallengeData2016/images/training/ADE_train_00013892.jpg'}
    '''

    testImagesFilenameList = create_image_lists(testImagesLocation)
    testAnotationsFilenameList = create_image_lists(testAnotationsLocation)
    trainImagesFilenameList = create_image_lists(trainImagesLocation)
    trainAnotationsFilenameList = create_image_lists(trainAnotationsLocation)

    training_records = []
    test_records = []

    assert(len(testImagesFilenameList) == len(testAnotationsFilenameList)), "Different number of test annotations from test images!"
    assert(len(trainImagesFilenameList) == len(trainAnotationsFilenameList)), "Different number of train annotations from test images!"

    for i in range(len(testImagesFilenameList)):
        test_records.append({})
        test_records[i]['annotation'] = testAnotationsFilenameList[i]
        test_records[i]['filename'] = testAnotationsFilenameList[i].split(".")[-2].split("/")[-1]
        test_records[i]['image'] = testImagesFilenameList[i]

    for i in range(len(trainImagesFilenameList)):
        training_records.append({})
        training_records[i]['annotation'] = trainAnotationsFilenameList[i]
        training_records[i]['filename'] = trainAnotationsFilenameList[i].split(".")[-2].split("/")[-1]
        training_records[i]['image'] = trainImagesFilenameList[i]
    
    return training_records, test_records


def create_image_lists(image_dir):
    filenames = []
    for root, dirs, files in os.walk(image_dir):
        filenames += glob.glob(os.path.join(root, '*.png'))

    return filenames
