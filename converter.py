import os
import ffmpeg
from yt_dlp import YoutubeDL

def download_tiktok_video(tiktok_url, output_video_path):
    """
    Use yt-dlp to download a TikTok video.
    """
    try:
        print(f"Downloading TikTok video from: {tiktok_url}")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': output_video_path,
            'quiet': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([tiktok_url])
        print(f"Video downloaded to: {output_video_path}")
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False

def convert_video_to_mp3(video_path, output_audio_path):
    """
    Convert a video file to MP3 using ffmpeg-python.
    """
    try:
        print(f"Converting {video_path} to {output_audio_path}...")
        (
            ffmpeg
            .input(video_path)
            .output(output_audio_path, format='mp3', acodec='libmp3lame')
            .run(quiet=True, overwrite_output=True)
        )
        print(f"Audio saved to: {output_audio_path}")
        return True
    except ffmpeg.Error as e:
        print("Error converting video to MP3:", e.stderr.decode())
        return False

def main():
    tiktok_url = input("Enter the TikTok URL: ")
    temp_video_path = "temp_video.mp4"
    output_audio_path = input("Enter the output MP3 file name (e.g., output.mp3): ")

    if download_tiktok_video(tiktok_url, temp_video_path):
        if convert_video_to_mp3(temp_video_path, output_audio_path):
            os.remove(temp_video_path)
            print("✅ Done!")
        else:
            print("❌ Failed to convert video to MP3.")
    else:
        print("❌ Failed to download TikTok video.")

if __name__ == "__main__":
    main()

