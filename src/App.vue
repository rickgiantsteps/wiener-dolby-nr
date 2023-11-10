<template>

  <header class="flex justify-center">
    <span class="dark:hidden width:500">
      <img class="z-10 ml-4 mt-3 mb-7" src="./components/icons/Logo_Politecnico_Milano-BLUE.png"  width="320" height="90" alt=""/>
          <div class="z-0 ml-2 absolute top-5 w-72 h-72 bg-[#6da4ba] rounded-full mix-blend-multiply filter blur-xl opacity-50 animate-blob"></div>
          <div class="z-0 ml-2 absolute top-5 w-72 h-72 bg-gray-50 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-blob animation-delay-2000"></div>
          <div class="z-0 ml-6 absolute top-5 w-72 h-72 bg-[#6da4ba] rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-4000"></div>
    </span>
    <span class="hidden dark:inline">
      <img class="z-10" src="./components/icons/Logo_Politecnico_Milano-WHITE.png" width="350" height="150" alt=""/>
           <div class="z-0 ml-2 absolute top-5 w-72 h-72 bg-white rounded-full filter blur-xl opacity-10 animate-blob"></div>
           <div class="z-0 ml-2 absolute top-5 w-72 h-72 bg-gray-50 rounded-full filter blur-xl opacity-20 animate-blob animation-delay-2000"></div>
           <div class="z-0 ml-6 absolute top-5 w-72 h-72 bg-[#6da4ba] rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"></div>
    </span>

    <div class="pl-5 dark:pl-0 relative flex items-center justify-between text-slate-700 font-semibold text-sm leading-6 dark:text-slate-200">
      <div class="flex absolute right-6 items-center">

        <a href="https://github.com/rickgiantsteps" target="_blank" rel="noopener noreferrer" class="mr-0 block text-slate-400 hover:text-slate-500 dark:hover:text-slate-300">
          <span class="sr-only">Our project on GitHub</span>
          <svg viewBox="0 0 16 16" class="w-5 h-5" fill="currentColor" aria-hidden="true">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
          </svg>
        </a>

        <div class="pl-3"></div>
        <label class="sr-only">Theme</label>

        <button type="button" @click="darkModeSwitch()">
        <span class="dark:hidden inline">
          <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6">
            <path d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" class="fill-[#6da4ba]/20 stroke-[#6da4ba]"></path>
            <path d="M12 4v1M17.66 6.344l-.828.828M20.005 12.004h-1M17.66 17.664l-.828-.828M12 20.01V19M6.34 17.664l.835-.836M3.995 12.004h1.01M6 6l.835.836" class="stroke-[#6da4ba]"></path>
          </svg>
        </span>
          <span class="hidden dark:inline">
          <svg viewBox="0 0 24 24" fill="none" class="w-6 h-6">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M17.715 15.15A6.5 6.5 0 0 1 9 6.035C6.106 6.922 4 9.645 4 12.867c0 3.94 3.153 7.136 7.042 7.136 3.101 0 5.734-2.032 6.673-4.853Z" class="fill-sky-400/20"></path>
            <path d="m17.715 15.15.95.316a1 1 0 0 0-1.445-1.185l.495.869ZM9 6.035l.846.534a1 1 0 0 0-1.14-1.49L9 6.035Zm8.221 8.246a5.47 5.47 0 0 1-2.72.718v2a7.47 7.47 0 0 0 3.71-.98l-.99-1.738Zm-2.72.718A5.5 5.5 0 0 1 9 9.5H7a7.5 7.5 0 0 0 7.5 7.5v-2ZM9 9.5c0-1.079.31-2.082.845-2.93L8.153 5.5A7.47 7.47 0 0 0 7 9.5h2Zm-4 3.368C5 10.089 6.815 7.75 9.292 6.99L8.706 5.08C5.397 6.094 3 9.201 3 12.867h2Zm6.042 6.136C7.718 19.003 5 16.268 5 12.867H3c0 4.48 3.588 8.136 8.042 8.136v-2Zm5.725-4.17c-.81 2.433-3.074 4.17-5.725 4.17v2c3.552 0 6.553-2.327 7.622-5.537l-1.897-.632Z" class="fill-[#ffffff]"></path>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M17 3a1 1 0 0 1 1 1 2 2 0 0 0 2 2 1 1 0 1 1 0 2 2 2 0 0 0-2 2 1 1 0 1 1-2 0 2 2 0 0 0-2-2 1 1 0 1 1 0-2 2 2 0 0 0 2-2 1 1 0 0 1 1-1Z" class="fill-[#ffffff]"></path>
          </svg>
        </span>
        </button>
      </div>
    </div>

  </header>

  <main>
    <div class="px-4 py-16 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:pb-1">
      <div class="grid gap-8 row-gap-5 lg:grid-cols-2">
        <div class="border-[#6da4ba] dark:hover:border-white hover:border-blue-100 relative p-px overflow-hidden transition duration-300 transform border rounded shadow-md hover:scale-105 group hover:shadow-lg dark:hover:shadow-white hover:shadow-blue-100 shadow-[#6da4ba]">
          <div class="absolute bottom-0 left-0 w-full h-1 duration-300 origin-left transform scale-x-0 bg-deep-purple-accent-400 group-hover:scale-x-100"></div>
          <div class="absolute bottom-0 left-0 w-1 h-full duration-300 origin-bottom transform scale-y-0 bg-deep-purple-accent-400 group-hover:scale-y-100"></div>
          <div class="absolute top-0 left-0 w-full h-1 duration-300 origin-right transform scale-x-0 bg-deep-purple-accent-400 group-hover:scale-x-100"></div>
          <div class="absolute bottom-0 right-0 w-1 h-full duration-300 origin-top transform scale-y-0 bg-deep-purple-accent-400 group-hover:scale-y-100"></div>
          <div class="relative p-5 bg-white dark:bg-gray-700 dark:text-white rounded-sm">
            <div class="flex flex-col mb-2 lg:items-center lg:flex-row">
              <div class="flex items-center justify-center w-10 h-10 mb-4 mr-2 rounded-full bg-indigo-50 lg:mb-0">
                <img class="object-cover" src="./components/icons/dolby.png">
              </div>
              <h6 class="font-extrabold leading-5 text-[#6da4ba] dark:text-white">Dolby-NR</h6>
            </div>
            <div class="w-50 h-16">
              <p class="mb-2 text-sm text-gray-900 dark:text-white">
                A Dolby noise-reduction system, or Dolby NR, is one of a series of noise reduction systems developed by Dolby Laboratories for use in analog audio tape recording.
              </p>
            </div>
          </div>
        </div>
        <div class="flex justify-center border-[#6da4ba] dark:hover:border-white hover:border-blue-100 relative p-px overflow-hidden transition duration-300 transform border rounded shadow-md hover:scale-105 group hover:shadow-lg dark:hover:shadow-white hover:shadow-blue-100 shadow-[#6da4ba]">
          <div class="absolute bottom-0 left-0 w-full h-1 duration-300 origin-left transform scale-x-0 bg-deep-purple-accent-400 group-hover:scale-x-100"></div>
          <div class="absolute bottom-0 left-0 w-1 h-full duration-300 origin-bottom transform scale-y-0 bg-deep-purple-accent-400 group-hover:scale-y-100"></div>
          <div class="absolute top-0 left-0 w-full h-1 duration-300 origin-right transform scale-x-0 bg-deep-purple-accent-400 group-hover:scale-x-100"></div>
          <div class="absolute bottom-0 right-0 w-1 h-full duration-300 origin-top transform scale-y-0 bg-deep-purple-accent-400 group-hover:scale-y-100"></div>
          <div class="relative p-5 bg-white bg-cover dark:bg-gray-700 dark:text-white rounded-sm">
            <div class="flex flex-col mb-2 lg:items-center lg:flex-row">
              <div class="w-10 h-10 mb-4 mr-2 rounded-full bg-indigo-50 lg:mb-0">
                <img class="object-cover" src="./components/icons/filter.png">
              </div>
              <h6 class="font-extrabold leading-5 text-[#6da4ba] dark:text-white ">Wiener Filter</h6>
            </div>
            <div class="w-50 h-16">
              <p class="mb-2 text-sm text-gray-900 dark:text-white">
                The Wiener filter is a filter used to produce an estimate of a desired or target random process by linear time-invariant (LTI) filtering of an observed noisy process, assuming known stationary signal and noise spectra, and additive noise.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="px-4 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 lg:pt-5">
      <div class="h-10 grid grid-rows-2 place-items-center mt-3 mb-11">
        <label for="songs" class="justify-center font-bold block mb-7 text-sm text-[#6da4ba] dark:text-white">Select a demo song</label>
        <select v-model="selected" id="songs" class="shadow-sm dark:shadow-white shadow-[#6da4ba] text-center w-64 justify-center bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-[#6da4ba] focus:border-[#6da4ba] block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-white dark:focus:border-white">
          <option value ="0">ABBA - Dancing Queen</option>
          <option value ="1">Aphex Twin - Alberto Balsalm</option>
          <option value ="2">Nirvana - Heart-Shaped Box</option>
          <option value ="3">Sade - Smooth Operator</option>
          <option value ="4" hidden></option>
        </select>
      </div>

      <div class="place-items-center grid grid-cols-3 gap-x-0">
        <audioplayer :selected="selected" @update="selectUpdate" @frame="songframed"></audioplayer>
        <form class="button-col">
          <button class="h-fit bg-[#6da4ba] dark:bg-slate-700 shadow-2xl shadow-[#6da4ba] hover:bg-slate-700 dark:hover:bg-slate-800 text-white font-bold py-2 px-4 rounded-full" @click="playNoise(noise)">Apply DOLBY NR</button>
          <!--<button id="buttonNoise" class="h-fit bg-[#6da4ba] dark:bg-slate-700 mt-2 shadow-2xl shadow-[#6da4ba] hover:bg-slate-700 dark:hover:bg-slate-800 text-white font-bold py-2 px-4 rounded-full" onclick="changeProperties()">Apply Noise</button> -->
          <button id="buttonNoise" class="h-fit mt-2 shadow-2xl shadow-[#6da4ba] font-bold py-2 px-4 rounded-full" @click="changeProperties()">Apply Noise</button>
        </form>
        <audioplayer download="true" secondplayer="true"></audioplayer>
      </div>

      <div class="flex justify-center mt-10">

        <div class="effects-choice-container dark:bg-slate-600 shadow shadow-[#6da4ba] dark:shadow-white">

          <label class="text-2xl font-bold flex justify-center text-[#6da4ba] dark:text-white mb-2">NOISE GENERATOR</label>
          <section class="synth-type">
            <button class="ml-3 w-5/6 mb-3 justify-center text-white font-bold py-2 px-4 rounded-full bg-[#6da4ba] shadow-sm shadow-[#6da4ba] dark:shadow-[#6da4ba] hover:bg-[#3e6f83]" @click="playNoise(noise)">Play noise</button>
            <button class="ml-3 w-5/6 mb-3 justify-center text-white font-bold py-2 px-4 rounded-full bg-[#6da4ba] shadow-sm shadow-[#6da4ba] dark:shadow-[#6da4ba] hover:bg-[#3e6f83]" @click="stopNoise(noise)">Stop</button>
            <div class="synth-selections shadow shadow-[#6da4ba] dark:shadow-white">
              <label class="text-base font-semibold text-[#6da4ba] dark:text-white ">White Noise</label>
              <div class="noise-slider-container dark:text-white">
                <section>
                  <input type="range"
                         v-model = "noise.volume"
                         @change = "setGain(noise)"
                         min="0"
                         max="0.1"
                         step="0.001"
                         class="input w-10 shadow shadow-[#6da4ba] dark:shadow-white"
                         id="am1">
                </section>
              </div>
              <label class="mt-28 text-base text-gray-900 dark:text-white mr-3">Gain</label>
            </div>

            <div class="synth-selections shadow shadow-[#6da4ba] dark:shadow-white ml-1">
              <label class="text-base font-semibold text-[#6da4ba] dark:text-white">HP Filter</label>
              <div class="synth-slider-container dark:text-white">
                <section>
                  <input type="range"
                         v-model = "filter.frequency"
                         @change = "setFilter(biquadFilter)"
                         min="1000"
                         max="8000"
                         step="10"
                         class="input2 w-10 shadow shadow-[#6da4ba] dark:shadow-white"
                         id="am2">
                </section>
                <section>
                  <input type="range"
                         v-model = "filter.gain"
                         @change = "setFilter(biquadFilter)"
                         min="-40"
                         max="40"
                         step="0.01"
                         class="input2 w-10 shadow shadow-[#6da4ba] dark:shadow-white"
                         id="am3">

                </section>
              </div>
              <div class="mt-28 two-col">
                <div class="col1">
                  <label class=" text-base text-gray-900 dark:text-white">Freq</label>
                </div>

                <div class="col2">
                  <label class="text-base text-gray-900 dark:text-white">Gain</label>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>


  </main>

  <footer class="flex justify-center">
    <p class="text-base p-6 dark:text-white">SASP Project - AY 2022/2023</p>
  </footer>
</template>

<script setup>
import "./assets/main.css"
import "./main.js"
import Audioplayer from "@/audioplayer.vue";


document.body.classList.toggle("bg-gray-50");

if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.classList.toggle("dark")
  document.body.classList.toggle("dark");
  document.body.classList.toggle("dark:bg-[#446573]");
}

function changeProperties() {
  var button = document.getElementById("buttonNoise");
  if (this.appliedNoise === false) {
    button.style.backgroundColor = "#446111"; // Change the background color
    button.style.color = "#FFF"; // Change the text color
    button.innerHTML = "Apply Noise"; // Change the button text
    this.appliedNoise=true;
  }else{
    button.style.backgroundColor = "#F00"; // Change the background color
    button.style.color = "#FFF"; // Change the text color
    button.innerHTML = "Clicked"; // Change the button text
    this.appliedNoise=false;
  }
}

function darkModeSwitch() {
  document.documentElement.classList.toggle("dark");
  document.body.classList.toggle("dark");
  document.body.classList.toggle("dark:bg-[#446573]");

  if (this.darkOn === false) {
    this.darkOn = true;
  } else if (this.darkOn === true) {
    this.darkOn = false;
  }
}
</script>

<script>
import * as fourier from 'fft-js'
const audioContext = new(window.AudioContext);
let windowsize = 1024
let zeropad_factor = windowsize * 4
let noiseanalyser = audioContext.createAnalyser();
export default {
  name: 'App',

  data() {
    return {
      biquadFilter: null,
      songframes: null,
      selected: "0",
      noise: {
        volume: 0.05, // 0 - 1
      },
      noisedata: Float32Array,
      fourierframes: [],
      timeframes: [],
      noisefourier: Float32Array,
      filter: {
        frequency: 2000,
        gain: 0
      },
      noisepower: null,
      songpower: null,
      out: Float32Array
    }
  },

  beforeMount() {
    this.buildTrack(this.noise);
    this.createNoise(this.noise);
    this.setGain(this.noise);
  },

  methods: {

    async freq_processing(track) {

      let emphfilt = []
      let deemphfilt = []
      let temporarysonglength = 10

      //takes too long, we need a loading interface

      //sometimes returns 0, needs time to fill noise data not consistent, noise should always be running
      //perhaps run but disconnected when not playing?
      await this.playNoise(this.noise)
      await new Promise(r => setTimeout(r, 1000));
      this.noisefourier = await fourier.fft(this.noisedata)
      this.stopNoise(this.noise)

      //get noisy song (clean song frames + noisedata)
      let noise_appoggio = this.noisedata
      let noisytrackframes = []
      for (let i = 0; i < track.length; i++) {
        noisytrackframes[i] = track[i].map(function (num, idx) {
          return num + noise_appoggio[idx];
        })
      }

      //frequency analysis of noisy song
      this.fourierframes = []

      for (let i=0; i<temporarysonglength; i++) {
        let track_array = []
        let track_appoggio = noisytrackframes[i]
        for(let ii = 0; ii < noisytrackframes[i].length; ii++){
          track_array[ii] = track_appoggio[ii]
        }
        this.fourierframes.push(fourier.fft(track_array.concat(Array(zeropad_factor-noisytrackframes[i].length).fill(0))))
      }


      this.noisepower = this.getpower(this.noisefourier,1)
      this.songpower = this.getpower(this.fourierframes,temporarysonglength)

      //filters, made 2d for correct product with signal fft
      for (let i = 0; i < this.songpower.length; i++) {
        emphfilt.push([Math.sqrt(this.noisepower[i] / this.songpower[i]),1]);
        deemphfilt.push([Math.sqrt((2*this.songpower[i]) / this.noisepower[i]),1]);
      }

      //filtering
      let filtered_song = []
      filtered_song = this.dolbyfiltering(this.fourierframes, emphfilt, deemphfilt)

      this.timeframes = []

      for (let i=0; i<filtered_song.length; i++) {
        this.timeframes.push(fourier.ifft(filtered_song[i]))
        //real values
        for(let ii = 0; ii < this.timeframes[i].length; ii++){
          this.timeframes[i][ii].pop()
          //turns length one float array into float value
          this.timeframes[i][ii] = parseFloat(this.timeframes[i][ii])
        }
      }

      console.log(this.timeframes)

      //     here add to out buffer, keeping track of the zero padding
      //     out_sd[int((k*hop)):int((k*hop + (zeropad_factor)))] += np.fft.ifft(his.timeframes[i])
      this.out = [0]
      //console.log(this.out)

      //file write

    },

    getpower(freqframes, n) {

      let power = [];
      let framepower = [];
      let ipower = []
      let undividedpow = new Array(4096).fill(0)

      if (n===1) {
        for (let i=0; i<freqframes.length; i++) {
          power[i] = Math.pow(freqframes[i][0],2)+Math.pow(freqframes[i][1],2)
        }
      } else {

        for (let i=0; i<n; i++) {
          framepower = []
          for(let ii = 0; ii < freqframes[i].length; ii++){
            framepower[ii] = Math.pow(freqframes[i][ii][0],2)+Math.pow(freqframes[i][ii][1],2)
          }
          ipower[i] = framepower
        }

        for (let i=0; i<ipower.length; i++) {
          undividedpow = undividedpow.map(function (num, idx) {
            return num + ipower[i][idx];
          });
        }

        for (let i = 0; i < undividedpow.length; i++) {
          power[i] = undividedpow[i] / n;
        }
      }

      return power
    },

    dolbyfiltering(freqdata, emphasis, deemphasis) {

      let filtered_song = []
      let filtered_song_frame = []
      let res1, res2

      console.log("dolby!")

      for (let i=0; i<freqdata.length; i++) {
        filtered_song_frame = []
        for (let k=0; k<freqdata[i].length; k++) {
          res1 = freqdata[i][k][0] * emphasis[k][0] * 0.5 * deemphasis[k][0]
          res2 = freqdata[i][k][1] * emphasis[k][1] * 0.5 * deemphasis[k][1]
          filtered_song_frame.push([res1, res2])
        }
        filtered_song.push(filtered_song_frame)
      }

      return filtered_song
    },


    createNoise(track) {

      const bufferSize = 2 * audioContext.sampleRate;
      const noiseBuffer = audioContext.createBuffer(1, bufferSize, audioContext.sampleRate);
      const output = noiseBuffer.getChannelData(0);

      for (let i = 0; i < bufferSize; i++) {
        output[i] = Math.random() * 2 - 1;
      }

      track.audioSource.buffer = noiseBuffer;
    },

    stopNoise(track) {
      try {
        if (track.audioSource) {
          track.audioSource.stop();
        }
      } catch(e) {}
    },

    buildTrack(track) {
      track.audioSource = audioContext.createBufferSource();
      track.gainNode = audioContext.createGain();
      this.biquadFilter = audioContext.createBiquadFilter();
      this.biquadFilter.type = "highpass";
      this.setFilter(this.biquadFilter)
      noiseanalyser.fftSize = zeropad_factor*2;
      track.audioSource.connect(track.gainNode);
      track.gainNode.connect(this.biquadFilter);
      this.biquadFilter.connect(noiseanalyser);
      noiseanalyser.connect(audioContext.destination)
    },

    setFilter(biquadFilter) {
      biquadFilter.frequency.setValueAtTime(this.filter.frequency, audioContext.currentTime);
      biquadFilter.gain.setValueAtTime(this.filter.gain, audioContext.currentTime);
    },

    setGain(track) {

      track.volume = (track.volume >= 0) ? track.volume : this.noise.volume;

      track.gainNode.gain.setValueAtTime(this.noise.volume, audioContext.currentTime);
    },

    getnoisedata() {
      const bufferLength = noiseanalyser.frequencyBinCount;
      const dataArray = new Float32Array(bufferLength);
      noiseanalyser.getFloatTimeDomainData(dataArray)
      return dataArray;
    },

    async playNoise(track) {
      this.stopNoise(track);
      this.buildTrack(track);
      this.createNoise(track);
      this.setGain(track);
      track.audioSource.loop = true;
      track.audioSource.start();

      //timeout not optimal
      //sometimes returns 0, needs time to fill noise data not consistent, noise should always be running
      //perhaps run but disconnected when not playing?
      await new Promise(r => setTimeout(r, 1000));
      this.noisedata = this.getnoisedata()
      console.log("noise:", this.noisedata)
    },

    selectUpdate (newData) {
      this.selected = newData
    },

    songframed (newFrames) {
      this.songframes = newFrames
      this.freq_processing(this.songframes, 0)
    }
  }
}

</script>