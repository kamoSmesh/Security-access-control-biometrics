from picamera2 import Picamera2 as PiCamera, Preview
import time


camera= PiCamera()

camera_config = camera.create_still_configuration(main={"size":(1920,1080)},lores={"size":(640,480)})
camera.configure(camera_config)
camera.start_preview(Preview.QTGL)
camera.start()

time.sleep(2)

camera.capture_file("test.jpg")
print('done')
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   
                                                                                   