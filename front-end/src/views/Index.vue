<template>
  <div class="fixed w-52 h-52 md:w-64 md:h-64 xl:w-96 xl:h-96 bg-primary -right-16 -top-20
   xl:-top-32 xl:-right-32  rounded-full "></div>

  <div class="dropdown dropdown-end fixed top-5 right-5 z-10">
    <label tabindex="0" class="btn btn-circle shadow-sm swap swap-rotate">

      <!-- this hidden checkbox controls the state -->
      <input type="checkbox" id="swap-options" @change="swapOption($event)">

      <!-- gear icon -->
      <CogIcon class="swap-off w-8 h-8" />
      <!-- close icon -->
      <XIcon class="swap-on w-8 h-8" />

    </label>
    <ul class="dropdown-content bg-base-100/50 w-60 shadow mt-3
        p-2 rounded-box backdrop-blur-lg" id="dropdown-options">
      <li class="text-sm font-bold text-gray-900">
        <span>Analyze option</span>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text text-gray-700">Whois</span>
            <input type="checkbox" class="toggle toggle-primary" checked>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text text-gray-700">GTmetrix</span>
            <input type="checkbox" class="toggle toggle-primary" checked>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text text-gray-700">Backlinks</span>
            <input type="checkbox" class="toggle toggle-primary" checked>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text text-gray-700">SSL</span>
            <input type="checkbox" class="toggle toggle-primary" checked>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text text-gray-700">AMP</span>
            <input type="checkbox" class="toggle toggle-primary" checked>
          </label>
        </div>
      </li>
    </ul>
  </div>
  <form class="flex flex-col items-center justify-center h-screen">

    <h1 class="text-4xl font-lato md:text-5xl xl:text-6xl font-black mb-2 md:mb-4 text-primary">
      Website Analyzer
    </h1>

    <input type="text" placeholder="exm: https://google.com/" name="url" class="input
        input-bordered input-primary w-3/6 xl:w-full max-w-xs input-md
        mb-4 md:mb-4 xl:mb-5">

    <button class="btn btn-primary text-center text-base-100">
      Analyze
    </button>

    <div class="list-disc mt-4 w-3/6 xl:w-full max-w-xs">
    </div>
  </form>

  <div class="fixed w-52 h-52 md:w-72 md:h-72 xl:w-80 xl:h-80 bg-primary -bottom-24 -left-20 rounded-full"></div>

</template>

<script>
import { CogIcon, XIcon } from '@heroicons/vue/outline';

export default {
  name: 'IndexPage',
  components: {
    CogIcon,
    XIcon,
  },
  methods: {
    swapOption(event) {
      const dropdownOptions = document.querySelector("#dropdown-options");

      const el = event.target

      if (el.checked) {
        dropdownOptions.style.visibility = "visible";
        dropdownOptions.style.opacity = "10";
      } else {
        dropdownOptions.style.visibility = "hidden";
        dropdownOptions.style.opacity = "0";
      }
    },
  },
}

</script>

<style >
.dropdown:not(.dropdown-hover):focus .dropdown-content,
.dropdown:not(.dropdown-hover):focus-within .dropdown-content {
  visibility: hidden;
  opacity: 0;
}


input[type=text] {
  outline: none;
}

input[type=text]:focus {
  box-shadow: 0 0 0 2px #5C7F67;
  outline: none;
}
</style>