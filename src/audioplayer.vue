<script setup>
import "./assets/audioplayer.scss"
</script>

<script>
import { defineComponent } from 'vue'
import * as mmb from 'music-metadata-browser';

export default defineComponent({
  name: 'audioplayer',

  props: {
    selected: String,
    download: false,
    secondplayer: false,
    downUrl: String
  },

  watch: {
    downUrl: {
      handler: function() {
        this.getProcessedSong();
      }
    },
    uploadedFile: {
      handler: function (newVal) {
        this.$emit('upload', newVal);
      }
    },
    selected: {
      handler: function () {
        this.songSelect()
      },
      deep: true
    },
    isTimerPlaying: {
      handler: function (newVal) {
        if (!this.secondplayer) {
          this.$emit('timer', newVal);
        }
        if (newVal&&!this.secondplayer&&this.$parent.$data.appliedNoise) {
          this.$emit('play');
        } else if (!this.secondplayer && this.$parent.$data.appliedNoise) {
          this.$emit('pause');
        }
      },
    }
  },

  data() {
    return {
      newname: "Unknown title",
      newartist: "Unknown artist",
      secondtrack: {
        artist: "DOLBY NR",
        name: "Denoised Version"
      },
      uploadedFile : null,
      audio: null,
      circleLeft: null,
      barWidth: null,
      duration: null,
      currentTime: null,
      isTimerPlaying: false,
      isTimerPlaying_second: false,
      tracks: [
        {
          name: "Dancing Queen",
          artist: "ABBA",
          source: "https://raw.githubusercontent.com/rickgiantsteps/wiener-dolby-nr/master/src/components/demo-songs/ABBA%20-%20Dancing%20Queen.mp3",
        },
        {
          name: "Alberto Balsalm",
          artist: "Aphex Twin",
          source: "https://raw.githubusercontent.com/rickgiantsteps/wiener-dolby-nr/master/src/components/demo-songs/Aphex%20Twin%20-%20Alberto%20Balsalm.mp3",
        },
        {
          name: "Heart-Shaped Box",
          artist: "Nirvana",
          source: "https://raw.githubusercontent.com/rickgiantsteps/wiener-dolby-nr/master/src/components/demo-songs/Nirvana%20-%20Heart-Shaped%20Box.mp3",
        },
        {
          name: "Smooth Operator",
          artist: "Sade",
          source: "https://raw.githubusercontent.com/rickgiantsteps/wiener-dolby-nr/master/src/components/demo-songs/Sade%20-%20Smooth%20Operator.mp3",
        },
        {
          name: "",
          artist: "",
          source: "",
        }
      ],
      currentTrack: null,
      currentTrackIndex: 0,
      transitionName: null,
      denoisedAudio: null
    };
  },

  methods: {

    async song_onFileChanged() {
      if (!this.secondplayer) {
        this.$emit("update", "5");
        this.uploadedFile = this.$refs.newsong.files[0];

        await mmb.parseBlob(this.uploadedFile).then(metadata => {
          this.newname = metadata.common.title;
          this.newartist = metadata.common.artist;
        });
        this.tracks.pop();
        if (this.newname === undefined && this.newartist === undefined) {
          this.newname = this.uploadedFile.name;
        }
        this.tracks.push({
          name: this.newname,
          artist: this.newartist,
          source: URL.createObjectURL(this.uploadedFile)
        });
        this.currentTrackIndex = this.tracks.length - 1;
        this.currentTrack = this.tracks[this.currentTrackIndex];
        this.generateTime();
        this.resetPlayer();
      }
    },


    async getProcessedSong() {
        if (this.secondplayer) {
          this.denoisedAudio = new Audio(this.downUrl);
          this.tracks.pop();
            this.tracks.push({
              name: "prova",
              artist: "prova",
              source: this.downUrl
            });

            this.currentTrackIndex = this.tracks.length - 1;
            this.currentTrack = this.tracks[this.currentTrackIndex];
            this.resetPlayer();

            console.log("Tracks: " + this.tracks);
            console.log("current track source: " + this.tracks[this.currentTrackIndex].source);
          }
        },

    async songSelect(){
      if (!this.secondplayer) {
        this.$emit("pause")
        this.$emit("update", this.selected)
        this.currentTrackIndex = this.selected
        this.currentTrack = this.tracks[this.selected];
        this.generateTime()
        this.resetPlayer()

        this.uploadedFile = await this.createFileObjectFromURL(this.currentTrack.source, this.currentTrack.artist+" - "+this.currentTrack.name+".mp3", "audio/*");
      }
    },

    createFileObjectFromURL(url, fileName, mimeType) {
      return fetch(url)
          .then(response => response.blob())
          .then(blob => new File([blob], fileName, { type: mimeType }));
    },

    async play() {
      if(!this.secondplayer) {
        if (this.audio.paused) {
          this.audio.play();
          this.isTimerPlaying = true;
        } else {
          this.audio.pause();
          this.isTimerPlaying = false;
        }
      }else{
        if (this.denoisedAudio.paused) {
          this.denoisedAudio.play();
          this.isTimerPlaying = true;
        } else {
          this.denoisedAudio.pause();
          this.isTimerPlaying = false;
        }

      }
    },

    

    generateTime() {
      if(!this.secondplayer) {
        let width = (100 / this.audio.duration) * this.audio.currentTime;
        this.barWidth = width + "%";
        this.circleLeft = width + "%";
        let durmin = Math.floor(this.audio.duration / 60);
        let dursec = Math.floor(this.audio.duration - durmin * 60);
        let curmin = Math.floor(this.audio.currentTime / 60);
        let cursec = Math.floor(this.audio.currentTime - curmin * 60);

        if (durmin < 10) {
          durmin = "0" + durmin;
        }
        if (dursec < 10) {
          dursec = "0" + dursec;
        }
        if (curmin < 10) {
          curmin = "0" + curmin;
        }
        if (cursec < 10) {
          cursec = "0" + cursec;
        }
        this.duration = durmin + ":" + dursec;
        this.currentTime = curmin + ":" + cursec;
      }else{
        let width = (100 / this.denoisedAudio.duration) * this.denoisedAudio.currentTime;
        this.barWidth = width + "%";
        this.circleLeft = width + "%";
        let durmin = Math.floor(this.denoisedAudio.duration / 60);
        let dursec = Math.floor(this.denoisedAudio.duration - durmin * 60);
        let curmin = Math.floor(this.denoisedAudio.currentTime / 60);
        let cursec = Math.floor(this.denoisedAudio.currentTime - curmin * 60);

        if (durmin < 10) {
          durmin = "0" + durmin;
        }
        if (dursec < 10) {
          dursec = "0" + dursec;
        }
        if (curmin < 10) {
          curmin = "0" + curmin;
        }
        if (cursec < 10) {
          cursec = "0" + cursec;
        }
        console.log("current time " + this.denoisedAudio.duration.currentTime);
        this.duration = durmin + ":" + dursec;
        this.currentTime = curmin + ":" + cursec;
      }
    },

    updateBar(x) {
      if(!this.secondplayer) {
        let progress = this.$refs.progress;
        let maxduration = this.audio.duration;
        let position = x - progress.offsetLeft;
        let percentage = (100 * position) / progress.offsetWidth;
        if (percentage > 100) {
          percentage = 100;
        }
        if (percentage < 0) {
          percentage = 0;
        }
        this.barWidth = percentage + "%";
        this.circleLeft = percentage + "%";
        this.audio.currentTime = (maxduration * percentage) / 100;
        this.audio.play();
      }else{
        let progress = this.$refs.progress;
        let maxduration = this.denoisedAudio.duration;
        let position = x - progress.offsetLeft;
        let percentage = (100 * position) / progress.offsetWidth;
        if (percentage > 100) {
          percentage = 100;
        }
        if (percentage < 0) {
          percentage = 0;
        }
        this.barWidth = percentage + "%";
        this.circleLeft = percentage + "%";
        this.denoisedAudio.currentTime = (maxduration * percentage) / 100;
        this.denoisedAudio.play();
      }
    },
    clickProgress(e) {
      this.isTimerPlaying = true;
      this.audio.pause();
      this.updateBar(e.pageX);
    },
    prevTrack() {
      this.transitionName = "scale-in";
      this.resetPlayer();
    },
    resetPlayer() {
      if(!this.secondplayer) {
        if (this.isTimerPlaying) {
          this.play()
        }
        this.barWidth = 0;
        this.circleLeft = 0;
        this.audio.currentTime = 0;
        this.audio.src = this.currentTrack.source;
        setTimeout(() => {
          if (this.isTimerPlaying) {
            this.audio.play();
          } else {
            this.audio.pause();
          }
        }, 300);
      }else{
        if (this.isTimerPlaying) {
          this.play()
        }
        this.barWidth = 0;
        this.circleLeft = 0;
        this.denoisedAudio.currentTime = 0;
        this.denoisedAudio.src = this.currentTrack.source;
        setTimeout(() => {
          if (this.isTimerPlaying) {
            this.denoisedAudio.play();
          } else {
            this.denoisedAudio.pause();
          }
        }, 300);
      }
    },


    downloadFile() {
      fetch('http://localhost:5000/api/get_denoised', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        responseType: 'blob',
      })
          .then(response => response.blob())
          .then(blob => {
            const url = URL.createObjectURL(blob);

            const link = document.createElement('a');
            link.href = url;
            link.download = 'denoised_audio.wav';

            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          })
          .catch(error => {
            console.error('Error downloading denoised audio', error);
          });
    }
  },

  async created() {
    if (!this.secondplayer) {
      let vm = this;
      this.currentTrack = this.tracks[0];
      this.audio = new Audio();
      this.audio.src = this.currentTrack.source;
      this.audio.ontimeupdate = function() {
        vm.generateTime();
      };
      this.audio.onloadedmetadata = function() {
        vm.generateTime();
      };
      this.audio.onended = function() {
        vm.audio.currentTime = 0
        vm.isTimerPlaying = false;
      };

      this.uploadedFile = await this.createFileObjectFromURL(this.currentTrack.source, this.currentTrack.artist+" - "+this.currentTrack.name+".mp3", "audio/*");
    }
  }
})
</script>

<template>
  <div class="grid grid-rows-2">
    <div v-if="download" class='file file--upload my-12'>
      <label @click="downloadFile" for='down-file'>
        <!--
        <svg viewBox="0 0 70 70" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
          <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
          <g id="SVGRepo_iconCarrier">
            <path d="M12 12V19M12 19L9.75 16.6667M12 19L14.25 16.6667M6.6 17.8333C4.61178 17.8333 3 16.1917 3 14.1667C3 12.498 4.09438 11.0897 5.59198 10.6457C5.65562 10.6268 5.7 10.5675 5.7 10.5C5.7 7.46243 8.11766 5 11.1 5C14.0823 5 16.5 7.46243 16.5 10.5C16.5 10.5582 16.5536 10.6014 16.6094 10.5887C16.8638 10.5306 17.1284 10.5 17.4 10.5C19.3882 10.5 21 12.1416 21 14.1667C21 16.1917 19.3882 17.8333 17.4 17.8333" stroke="#464455" stroke-linecap="round" stroke-linejoin="round">
          </path>
          </g>
        </svg>
        Download audio file        -->
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cloud-arrow-down-fill" viewBox="0 0 16 16"> <path d="M8 2a5.53 5.53 0 0 0-3.594 1.342c-.766.66-1.321 1.52-1.464 2.383C1.266 6.095 0 7.555 0 9.318 0 11.366 1.708 13 3.781 13h8.906C14.502 13 16 11.57 16 9.773c0-1.636-1.242-2.969-2.834-3.194C12.923 3.999 10.69 2 8 2zm2.354 6.854-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 1 1 .708-.708L7.5 9.293V5.5a.5.5 0 0 1 1 0v3.793l1.146-1.147a.5.5 0 0 1 .708.708z"/> </svg> ⠀
        Download audio file
      </label>
      <button ref="downsong" id='down-file'/>
    </div>
    <div v-else class='file file--upload'>
      <label for='input-file'>
        <!--<svg class="icon">
          <use xlink:href="#icon-cloud"></use>
        </svg> -->
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cloud-arrow-up-fill mr-3" viewBox="0 0 16 16"> <path d="M8 2a5.53 5.53 0 0 0-3.594 1.342c-.766.66-1.321 1.52-1.464 2.383C1.266 6.095 0 7.555 0 9.318 0 11.366 1.708 13 3.781 13h8.906C14.502 13 16 11.57 16 9.773c0-1.636-1.242-2.969-2.834-3.194C12.923 3.999 10.69 2 8 2zm2.354 5.146a.5.5 0 0 1-.708.708L8.5 6.707V10.5a.5.5 0 0 1-1 0V6.707L6.354 7.854a.5.5 0 1 1-.708-.708l2-2a.5.5 0 0 1 .708 0l2 2z"/> </svg>
        Upload audio file
      </label>
      <input v-on:change="song_onFileChanged" ref="newsong" id='input-file' type="file" accept="audio/*"/>
    </div>
    <div class="player">
      <div class="player__top">
        <div class="player-controls">
          <div>
            <div class="album-info" v-if="!secondplayer">
              <div class="album-info__name">{{ currentTrack.artist }}</div>
              <div class="album-info__track">{{ currentTrack.name }}</div>
            </div>
            <div class="album-info" v-else>
              <div class="album-info__name">{{ secondtrack.artist }}</div>
              <div class="album-info__track">{{ secondtrack.name }}</div>
            </div>
            <div class="player-controls__item" @click="prevTrack">
              <svg class="icon">
                <use xlink:href="#icon-prev"></use>
              </svg>
            </div>
            <div class="player-controls__item -xl js-play" @click="play">
              <svg class="icon">
                <use xlink:href="#icon-pause" v-if="isTimerPlaying"></use>
                <use xlink:href="#icon-play" v-else></use>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="progress" ref="progress">
        <div class="progress__top">
          <div class="progress__duration">{{ duration }}</div>
        </div>
        <div class="progress__bar" @click="clickProgress">
          <div class="progress__current" :style="{ width : barWidth }"></div>
        </div>
        <div class="progress__time">{{ currentTime }}</div>
      </div>
      <div v-cloak></div>
    </div>
  </div>

  <svg xmlns="http://www.w3.org/2000/svg" hidden xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
      <symbol id="icon-cloud" viewBox="0 0 24 24">
        <title>icon-cloud</title>
        <path d="M0 0h24v24H0z" fill="none"/>
        <path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"/>
      </symbol>

      <symbol id="icon-pause" viewBox="0 0 32 32">
        <title>icon-pause</title>
        <path d="M16 0.32c-8.64 0-15.68 7.040-15.68 15.68s7.040 15.68 15.68 15.68 15.68-7.040 15.68-15.68-7.040-15.68-15.68-15.68zM16 29.216c-7.296 0-13.216-5.92-13.216-13.216s5.92-13.216 13.216-13.216 13.216 5.92 13.216 13.216-5.92 13.216-13.216 13.216z"></path>
        <path d="M16 32c-8.832 0-16-7.168-16-16s7.168-16 16-16 16 7.168 16 16-7.168 16-16 16zM16 0.672c-8.448 0-15.328 6.88-15.328 15.328s6.88 15.328 15.328 15.328c8.448 0 15.328-6.88 15.328-15.328s-6.88-15.328-15.328-15.328zM16 29.568c-7.488 0-13.568-6.080-13.568-13.568s6.080-13.568 13.568-13.568c7.488 0 13.568 6.080 13.568 13.568s-6.080 13.568-13.568 13.568zM16 3.104c-7.104 0-12.896 5.792-12.896 12.896s5.792 12.896 12.896 12.896c7.104 0 12.896-5.792 12.896-12.896s-5.792-12.896-12.896-12.896z"></path>
        <path d="M12.16 22.336v0c-0.896 0-1.6-0.704-1.6-1.6v-9.472c0-0.896 0.704-1.6 1.6-1.6v0c0.896 0 1.6 0.704 1.6 1.6v9.504c0 0.864-0.704 1.568-1.6 1.568z"></path>
        <path d="M19.84 22.336v0c-0.896 0-1.6-0.704-1.6-1.6v-9.472c0-0.896 0.704-1.6 1.6-1.6v0c0.896 0 1.6 0.704 1.6 1.6v9.504c0 0.864-0.704 1.568-1.6 1.568z"></path>
      </symbol>
      <symbol id="icon-play" viewBox="0 0 32 32">
        <title>icon-play</title>
        <path d="M21.216 15.168l-7.616-5.088c-0.672-0.416-1.504 0.032-1.504 0.832v10.176c0 0.8 0.896 1.248 1.504 0.832l7.616-5.088c0.576-0.416 0.576-1.248 0-1.664z"></path>
        <path d="M13.056 22.4c-0.224 0-0.416-0.064-0.608-0.16-0.448-0.224-0.704-0.672-0.704-1.152v-10.176c0-0.48 0.256-0.928 0.672-1.152s0.928-0.224 1.344 0.064l7.616 5.088c0.384 0.256 0.608 0.672 0.608 1.088s-0.224 0.864-0.608 1.088l-7.616 5.088c-0.192 0.16-0.448 0.224-0.704 0.224zM13.056 10.272c-0.096 0-0.224 0.032-0.32 0.064-0.224 0.128-0.352 0.32-0.352 0.576v10.176c0 0.256 0.128 0.48 0.352 0.576 0.224 0.128 0.448 0.096 0.64-0.032l7.616-5.088c0.192-0.128 0.288-0.32 0.288-0.544s-0.096-0.416-0.288-0.544l-7.584-5.088c-0.096-0.064-0.224-0.096-0.352-0.096z"></path>
        <path d="M16 0.32c-8.64 0-15.68 7.040-15.68 15.68s7.040 15.68 15.68 15.68 15.68-7.040 15.68-15.68-7.040-15.68-15.68-15.68zM16 29.216c-7.296 0-13.216-5.92-13.216-13.216s5.92-13.216 13.216-13.216 13.216 5.92 13.216 13.216-5.92 13.216-13.216 13.216z"></path>
        <path d="M16 32c-8.832 0-16-7.168-16-16s7.168-16 16-16 16 7.168 16 16-7.168 16-16 16zM16 0.672c-8.448 0-15.328 6.88-15.328 15.328s6.88 15.328 15.328 15.328c8.448 0 15.328-6.88 15.328-15.328s-6.88-15.328-15.328-15.328zM16 29.568c-7.488 0-13.568-6.080-13.568-13.568s6.080-13.568 13.568-13.568c7.488 0 13.568 6.080 13.568 13.568s-6.080 13.568-13.568 13.568zM16 3.104c-7.104 0-12.896 5.792-12.896 12.896s5.792 12.896 12.896 12.896c7.104 0 12.896-5.792 12.896-12.896s-5.792-12.896-12.896-12.896z"></path>
      </symbol>
      <symbol id="icon-prev" viewBox="0 0 32 32">
        <title>prev</title>
        <path d="M29.696 13.696h-14.688l4.576-4.576c0.864-0.864 0.864-2.336 0-3.232-0.864-0.864-2.336-0.864-3.232 0l-8.448 8.48c-0.864 0.864-0.864 2.336 0 3.232l8.448 8.448c0.448 0.448 1.056 0.672 1.632 0.672s1.184-0.224 1.632-0.672c0.864-0.864 0.864-2.336 0-3.232l-4.608-4.576h14.688c1.248 0 2.304-1.024 2.304-2.304s-1.024-2.24-2.304-2.24z"></path>
        <path d="M2.304 5.248c-1.248 0-2.304 1.024-2.304 2.304v16.928c0 1.248 1.024 2.304 2.304 2.304s2.304-1.024 2.304-2.304v-16.928c-0.064-1.28-1.056-2.304-2.304-2.304z"></path>
      </symbol>
      <symbol id="icon-link" viewBox="0 0 32 32">
        <title>link</title>
        <path d="M23.584 17.92c0 0.864 0 1.728 0 2.56 0 1.312 0 2.656 0 3.968 0 0.352 0.032 0.736-0.032 1.12 0.032-0.16 0.032-0.288 0.064-0.448-0.032 0.224-0.096 0.448-0.16 0.64 0.064-0.128 0.128-0.256 0.16-0.416-0.096 0.192-0.192 0.384-0.32 0.576 0.096-0.128 0.16-0.224 0.256-0.352-0.128 0.16-0.288 0.32-0.48 0.48 0.128-0.096 0.224-0.16 0.352-0.256-0.192 0.128-0.352 0.256-0.576 0.32 0.128-0.064 0.256-0.128 0.416-0.16-0.224 0.096-0.416 0.16-0.64 0.16 0.16-0.032 0.288-0.032 0.448-0.064-0.256 0.032-0.512 0.032-0.768 0.032-0.448 0-0.896 0-1.312 0-1.472 0-2.976 0-4.448 0-1.824 0-3.616 0-5.44 0-1.568 0-3.104 0-4.672 0-0.736 0-1.44 0-2.176 0-0.128 0-0.224 0-0.352-0.032 0.16 0.032 0.288 0.032 0.448 0.064-0.224-0.032-0.448-0.096-0.64-0.16 0.128 0.064 0.256 0.128 0.416 0.16-0.192-0.096-0.384-0.192-0.576-0.32 0.128 0.096 0.224 0.16 0.352 0.256-0.16-0.128-0.32-0.288-0.48-0.48 0.096 0.128 0.16 0.224 0.256 0.352-0.128-0.192-0.256-0.352-0.32-0.576 0.064 0.128 0.128 0.256 0.16 0.416-0.096-0.224-0.16-0.416-0.16-0.64 0.032 0.16 0.032 0.288 0.064 0.448-0.032-0.256-0.032-0.512-0.032-0.768 0-0.448 0-0.896 0-1.312 0-1.472 0-2.976 0-4.448 0-1.824 0-3.616 0-5.44 0-1.568 0-3.104 0-4.672 0-0.736 0-1.44 0-2.176 0-0.128 0-0.224 0.032-0.352-0.032 0.16-0.032 0.288-0.064 0.448 0.032-0.224 0.096-0.448 0.16-0.64-0.064 0.128-0.128 0.256-0.16 0.416 0.096-0.192 0.192-0.384 0.32-0.576-0.096 0.128-0.16 0.224-0.256 0.352 0.128-0.16 0.288-0.32 0.48-0.48-0.128 0.096-0.224 0.16-0.352 0.256 0.192-0.128 0.352-0.256 0.576-0.32-0.128 0.064-0.256 0.128-0.416 0.16 0.224-0.096 0.416-0.16 0.64-0.16-0.16 0.032-0.288 0.032-0.448 0.064 0.48-0.064 0.96-0.032 1.44-0.032 0.992 0 1.952 0 2.944 0 1.216 0 2.432 0 3.616 0 1.056 0 2.112 0 3.168 0 0.512 0 1.024 0 1.536 0 0 0 0 0 0.032 0 0.448 0 0.896-0.192 1.184-0.48s0.512-0.768 0.48-1.184c-0.032-0.448-0.16-0.896-0.48-1.184s-0.736-0.48-1.184-0.48c-0.64 0-1.28 0-1.92 0-1.408 0-2.816 0-4.224 0-1.44 0-2.848 0-4.256 0-0.672 0-1.344 0-2.016 0-0.736 0-1.472 0.192-2.112 0.576s-1.216 0.96-1.568 1.6c-0.384 0.64-0.544 1.376-0.544 2.144 0 0.672 0 1.376 0 2.048 0 1.28 0 2.56 0 3.84 0 1.504 0 3.040 0 4.544 0 1.408 0 2.848 0 4.256 0 0.992 0 1.952 0 2.944 0 0.224 0 0.448 0 0.64 0 0.864 0.224 1.76 0.768 2.464 0.16 0.192 0.288 0.384 0.48 0.576s0.384 0.352 0.608 0.512c0.32 0.224 0.64 0.384 1.024 0.512 0.448 0.16 0.928 0.224 1.408 0.224 0.16 0 0.32 0 0.48 0 0.896 0 1.792 0 2.72 0 1.376 0 2.784 0 4.16 0 1.536 0 3.040 0 4.576 0 1.312 0 2.656 0 3.968 0 0.768 0 1.536 0 2.336 0 0.416 0 0.832-0.032 1.248-0.128 1.504-0.32 2.784-1.6 3.104-3.104 0.128-0.544 0.128-1.056 0.128-1.568 0-0.608 0-1.184 0-1.792 0-1.408 0-2.816 0-4.224 0-0.256 0-0.512 0-0.768 0-0.448-0.192-0.896-0.48-1.184s-0.768-0.512-1.184-0.48c-0.448 0.032-0.896 0.16-1.184 0.48-0.384 0.384-0.576 0.768-0.576 1.248v0z"></path>
        <path d="M32 11.232c0-0.8 0-1.568 0-2.368 0-1.248 0-2.528 0-3.776 0-0.288 0-0.576 0-0.864 0-0.896-0.768-1.696-1.696-1.696-0.8 0-1.568 0-2.368 0-1.248 0-2.528 0-3.776 0-0.288 0-0.576 0-0.864 0-0.448 0-0.896 0.192-1.184 0.48s-0.512 0.768-0.48 1.184c0.032 0.448 0.16 0.896 0.48 1.184s0.736 0.48 1.184 0.48c0.8 0 1.568 0 2.368 0 1.248 0 2.528 0 3.776 0 0.288 0 0.576 0 0.864 0-0.576-0.576-1.12-1.12-1.696-1.696 0 0.8 0 1.568 0 2.368 0 1.248 0 2.528 0 3.776 0 0.288 0 0.576 0 0.864 0 0.448 0.192 0.896 0.48 1.184s0.768 0.512 1.184 0.48c0.448-0.032 0.896-0.16 1.184-0.48 0.352-0.256 0.544-0.64 0.544-1.12v0z"></path>
        <path d="M15.040 21.888c0.16-0.16 0.288-0.288 0.448-0.448 0.384-0.384 0.8-0.8 1.184-1.184 0.608-0.608 1.184-1.184 1.792-1.792 0.704-0.704 1.44-1.44 2.176-2.176 0.8-0.8 1.568-1.568 2.368-2.368s1.6-1.6 2.4-2.4c0.736-0.736 1.504-1.504 2.24-2.24 0.64-0.64 1.248-1.248 1.888-1.888 0.448-0.448 0.896-0.896 1.344-1.344 0.224-0.224 0.448-0.416 0.64-0.64 0 0 0.032-0.032 0.032-0.032 0.32-0.32 0.48-0.768 0.48-1.184s-0.192-0.896-0.48-1.184c-0.32-0.288-0.736-0.512-1.184-0.48-0.512 0.032-0.928 0.16-1.248 0.48-0.16 0.16-0.288 0.288-0.448 0.448-0.384 0.384-0.8 0.8-1.184 1.184-0.608 0.608-1.184 1.184-1.792 1.792-0.704 0.704-1.44 1.44-2.176 2.176-0.8 0.8-1.568 1.568-2.368 2.368s-1.6 1.6-2.4 2.4c-0.736 0.736-1.504 1.504-2.24 2.24-0.64 0.64-1.248 1.248-1.888 1.888-0.448 0.448-0.896 0.896-1.344 1.344-0.224 0.224-0.448 0.416-0.64 0.64 0 0-0.032 0.032-0.032 0.032-0.32 0.32-0.48 0.768-0.48 1.184s0.192 0.896 0.48 1.184c0.32 0.288 0.736 0.512 1.184 0.48 0.48 0 0.928-0.16 1.248-0.48v0z"></path>
      </symbol>
    </defs>
  </svg>
</template>

<style scoped>

</style>