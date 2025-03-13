# Solution to solve the challenge

## Download the challenge file.

![Screenshot 2025-03-13 181940.png](Screenshot_2025-03-13_181940.png)

## Extract the downloaded file

![Screenshot 2025-03-13 181100.png](Screenshot_2025-03-13_181100.png)

![Screenshot 2025-03-13 182114.png](Screenshot_2025-03-13_182114.png)

- We get a file named secret which is an image.
- Ok we got a message here “Hey did you listen to that??”.
- Use ExifTool to display the meta data.
- We have an encoded text in the user comments.

## Now lets decode the text which seems to be base64 encoded.

![Screenshot 2025-03-13 181142.png](Screenshot_2025-03-13_181142.png)

- “Walk toward the bin.” - This maybe a hint to use binwalk

Using Binwalk to extract the hidden files

![Screenshot 2025-03-13 181401.png](Screenshot_2025-03-13_181401.png)

- We got a hidden file named spot_me.mp3
- Now the message “hey did you listen to that make sense.”

## Open the mp3 file in a music visualizer like audacity/sonic visualiser

![Screenshot 2025-03-13 181609.png](Screenshot_2025-03-13_181609.png)

- We have an audio clip of JOHN CENA’s entrance music!

## Change the view from waveform to spectrogram

![Screenshot 2025-03-13 181526.png](Screenshot_2025-03-13_181526.png)

- Here we go - flag{y0u_c4n_s33_m3} :)
