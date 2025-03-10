import sys
import random
import argparse

if sys.platform == 'darwin':
    sys.path.append('MovingObjectDetector')
    sys.path.append('TrainNetwork')
    sys.path.append('SimpleTracker')
    #Specify DeepConcolic src file here:
    sys.path.append('../DeepConcolic/src')
    from MOD_BaseFunctions import createImageDirectory
    from run_detection_main import run_detection_main
else:
    sys.path.append('DeepConcolic/src')
    from MovingObjectDetector.MOD_BaseFunctions import createImageDirectory
    from MovingObjectDetector.run_detection_main import run_detection_main


def running(attack, model_folder, imagefolder, input_image_idx, ROI_centre, writeimagefolder0, ROI_window, num_of_template):

    instance = "%s_%s_%s/"%(input_image_idx, ROI_centre[0], ROI_centre[1])
    writeimagefolder = writeimagefolder0 + instance
    createImageDirectory(writeimagefolder)
    run_detection_main(attack, model_folder, imagefolder, input_image_idx, ROI_centre, writeimagefolder, ROI_window, num_of_template)


def main():

    parser = argparse.ArgumentParser(description='Verification and Validation of WAMI Tracking' )
    parser.add_argument(
      '--image-index', dest='input_image_idx', default='10', help='the index of the input image in WASABI dataset')
    parser.add_argument("--attack", dest="attack", default="classification",
                      help="attack or not")
    parser.add_argument("--ROI_centre", dest="ROI_centre", default="4500, 5000",
                      help="ROI_centre")
    #parser.add_argument("--output-image-folder", dest="writeimagefolder0", default="savefig/",
    #                  help="ROI_centre")
    parser.add_argument("--output-image-folder", dest="writeimagefolder0", default="C:/Workspace-python/savefig/",
                      help="ROI_centre")
    #parser.add_argument("--wasabi-image-folder", dest="imagefolder", default="/Users/xiaowei/Dropbox/wasabi-detection-python-new/WAPAFB_images_train/training/",
    #                  help="ROI_centre")
    parser.add_argument("--wasabi-image-folder", dest="imagefolder", default="C:/WPAFB-images/training/",
                      help="ROI_centre")
    parser.add_argument("--deepconcolic-folder", dest="deepconcolic", default="../DeepConcolic/src/",
                      help="ROI_centre")
    parser.add_argument(
      '--ROI_window', dest='ROI_window', default='1000', help='the windows size of ROI')
    parser.add_argument(
      '--num_of_template', dest='num_of_template', default='3', help='num of templates for [...]')

    args = parser.parse_args()

    attack = args.attack
    input_image_idx = int(''.join(x for x in args.input_image_idx if x.isdigit()))
    ROI_window = int(''.join(x for x in args.ROI_window if x.isdigit()))
    num_of_template = int(''.join(x for x in args.num_of_template if x.isdigit()))
    l,r = args.ROI_centre.split(",")
    ln = ''.join(x for x in l if x.isdigit())
    rn = ''.join(x for x in r if x.isdigit())
    ROI_centre = [int(ln), int(rn)]

    model_folder = "Models/"
    imagefolder = args.imagefolder

    running(attack, model_folder, imagefolder, input_image_idx, ROI_centre, args.writeimagefolder0, ROI_window, num_of_template)
'''
    for t in range(1000): 
        x = random.randint(3000,6000)
        y = random.randint(3000,6000)
        ROI_centre = [x,y]
        print("**************** start working on (%s,%s)..."%(str(x),str(y)))
        running(attack,model_folder,imagefolder,input_image_idx,ROI_centre,args.writeimagefolder0,ROI_window,num_of_template)
'''
if __name__=="__main__":
  main()


