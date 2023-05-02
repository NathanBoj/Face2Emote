#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install deepface')
get_ipython().system('pip install requests')
get_ipython().system('pip install irc')

import cv2
import os
import time
from deepface import DeepFace
from twitchio.ext import commands

Access_Token = input("ACCESS TOKEN: ")
Twitch_Channel = input("Twitch channel you want to join: ")

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=Access_Token, prefix='?', initial_channels=[Twitch_Channel])
        
    async def send_message(self, message: str, channel: str):
        # Send a message to the specified channel
        await self.get_channel(channel).send(message)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

        # Send a message to the desired channel
        message = "Connected to chat!"
        await self.send_message(message, Twitch_Channel)

        # The bot is now ready, you can call `send_message()` or other methods safely here
        
        # create the 'faces' directory if it does not exist
        if not os.path.exists('faces'):
            os.makedirs('faces')

        # initialize the webcam
        cap = cv2.VideoCapture(0)

        # set the resolution of the webcam
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # set the initial counter to 1
        counter = 1

        # set the initial emotion
        emotion = ""
        
        # get current time
        start_time = time.time() 
        
        # continuously capture frames from the webcam
        while True:
            # capture a frame
            ret, frame = cap.read()

            # if the frame was successfully captured
            if ret:

                current_time = time.time()  # get current time
                elapsed_time = current_time - start_time  # calculate elapsed time

                # put the countdown timer on the frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                cv2.putText(frame, f'Next photo in {round(10-elapsed_time)}s, Emotion: {emotion}', (20, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.putText(frame, f'q to exit', (20, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

                # show the frame to the user
                cv2.imshow('Webcam', frame)

                if elapsed_time >= 10:
                    # check if 10 seconds have elapsed and last message was sent more than 10 seconds ago
                    print("10 seconds have passed!")
                    start_time = current_time  # update last message time

                    # save the frame to a file
                    filename = os.path.join('faces', f'{counter}.jpg')
                    cv2.imwrite(filename, frame)
                    print(f'Saved photo {counter}')

                    try:
                        objs = DeepFace.analyze(img_path=filename, actions=['emotion'])

                        emotion = max(objs[0]['emotion'], key=objs[0]['emotion'].get)

                        # Use a switch statement to handle different emotions
                        switch_case = {
                            'disgust': 'DansGame',
                            'fear': 'monkaW',
                            'happy': 'FeelsStrongMan',
                            'sad': 'SAJ',
                            'surprise': 'OMEGALUL',
                            'neutral': 'PepeNPC'
                        }

                        response = switch_case.get(emotion, 'not detected')

                        print(response)
                        
                        await self.send_message(response, Twitch_Channel)

                    except Exception as e:
                        # handle the error
                        print("An error occurred:", e)
                        emotion = "not detected"

                    # increment the counter
                    counter += 1

            # if the user presses the 'q' key, exit the loop
            if cv2.waitKey(1) == ord('q'):
                break

            time.sleep(0.1)  # wait for 0.1 seconds to avoid busy-waiting

        # release the webcam and close the window
        cap.release()
        cv2.destroyAllWindows()

bot = Bot()
bot.run()


# In[ ]:




