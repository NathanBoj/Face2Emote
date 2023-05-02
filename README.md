# Face2Emote
- Connect your webcam and twitch to chat!
- Takes your webcam's video stream and takes a picture every 10 seconds, [deepface](https://github.com/serengil/deepface) predicts your faces mood and uses [TwitchIO](https://github.com/TwitchIO/TwitchIO) to send a messages on behalf of your Twitch account.

Dependencies:
- !pip install deepface
- !pip install requests
- !pip install irc

Visit [Token Generator](https://twitchtokengenerator.com/) for a simple way to generate your ACCESS TOKEN.

<img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/ui.png" >

If you want to change the emotes to your preferences, edit this section in main.py (need to recompile saj)

<img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/change.png" >

<img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/example.png" >

<img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/1.jpg" >

### Future improvements:
- sunglasses = <img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/ez.jpg" width="3%" height="3%" >
- hand on head, hand on waist = <img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/pot.jpg" width="3%" height="3%"  >
- heart hand = <img src="https://github.com/NathanBoj/Face2Emote/blob/main/images/xqcl.jpg" width="3%" height="3%" >
