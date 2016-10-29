import sys, os, time
import api
import time
import threading
import sound
import emotionDisplay

class emotion():
    def emotion_ready(self):
        if api.Initialize():
            print("Initialized")
            api.PlayAction(3)
            time.sleep(3)
        else:
            print("Initialization failed")
            sys.exit(1)

    def show_emotion(self, emtion_class, emotion_level):
        # gesture_thread = threading.Thread(target = api.PlayAction(4))
        # test_thread = threading.Thread(target = self.test_helper())
        # facial_thread = threading.Thread(target = emotionDisplay.main())
        # sound_thread = threading.Thread(target = sound.sound_activate('happy',2))

        api_map = {'happy3': 4, 'happy2': 5, 'anger2': 6, 'anger3': 7, 'fear3': 11,
                   'fear2': 12, 'surprise2': 13, 'surprise3': 14, 'sad2': 17, 'sad3': 18}


        # facial_thread.start()
        # sound_thread.start()
        emotionDisplay.main()
        sound.sound_activate(emtion_class, emotion_level)
        api.PlayAction(api_map[emtion_class + repr(emotion_level)])

    def emotion_finished(self):
        api.ServoShutdown()

    def test_helper(self):
        print 'test thread'



if __name__ == '__main__':
    new_emotion = emotion()
    new_emotion.emotion_ready()
    new_emotion.show_emotion(sys.argv[1], int(sys.argv[2]))
    new_emotion.emotion_finished()
