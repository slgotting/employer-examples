

export function playSound(audioElement, volume=0.3) {
    // handles restarting the sound if its already playing
    audioElement.volume = volume
    audioElement.pause();
    audioElement.currentTime = 0;
    audioElement.play();
}