from moviepy.editor import VideoFileClip, AudioFileClip

# Load your video
video = VideoFileClip("input_video.mp4")

# Load your new dubbed audio
audio = AudioFileClip("dubbed_audio.mp3")

# Replace the original audio with the dubbed audio
final_video = video.set_audio(audio)

# Export the final video
final_video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

print("Video dubbing complete!")
