function playAudioAndVideo() {
    var audio = document.getElementById("audio");
    audio.volume = 0.4;
    audio.play();

    var video = document.getElementById("video");
    video.play();
}