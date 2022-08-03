<template>
  <div class="fixed w-52 h-52 md:w-64 md:h-64 xl:w-96 xl:h-96 bg-primary -right-16 -top-20
   xl:-top-32 xl:-right-32  rounded-full "></div>

  <div class="dropdown dropdown-end dropdown-hover fixed top-5 right-5 z-10">
    <label tabindex="0" class="btn btn-circle swap swap-rotate">

      <!-- this hidden checkbox controls the state -->
      <input type="checkbox" id="swap-options">

      <!-- gear icon -->
      <svg class="swap-off fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
        <path d="M25 34c-5 0-9-4-9-9s4-9 9-9 9 4 9 9-4 9-9 9zm0-16c-3.9 0-7 3.1-7 7s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7z" />
        <path
          d="M27.7 44h-5.4l-1.5-4.6c-1-.3-2-.7-2.9-1.2l-4.4 2.2-3.8-3.8 2.2-4.4c-.5-.9-.9-1.9-1.2-2.9L6 27.7v-5.4l4.6-1.5c.3-1 .7-2 1.2-2.9l-2.2-4.4 3.8-3.8 4.4 2.2c.9-.5 1.9-.9 2.9-1.2L22.3 6h5.4l1.5 4.6c1 .3 2 .7 2.9 1.2l4.4-2.2 3.8 3.8-2.2 4.4c.5.9.9 1.9 1.2 2.9l4.6 1.5v5.4l-4.6 1.5c-.3 1-.7 2-1.2 2.9l2.2 4.4-3.8 3.8-4.4-2.2c-.9.5-1.9.9-2.9 1.2L27.7 44zm-4-2h2.6l1.4-4.3.5-.1c1.2-.3 2.3-.8 3.4-1.4l.5-.3 4 2 1.8-1.8-2-4 .3-.5c.6-1 1.1-2.2 1.4-3.4l.1-.5 4.3-1.4v-2.6l-4.3-1.4-.1-.5c-.3-1.2-.8-2.3-1.4-3.4l-.3-.5 2-4-1.8-1.8-4 2-.5-.3c-1.1-.6-2.2-1.1-3.4-1.4l-.5-.1L26.3 8h-2.6l-1.4 4.3-.5.1c-1.2.3-2.3.8-3.4 1.4l-.5.3-4-2-1.8 1.8 2 4-.3.5c-.6 1-1.1 2.2-1.4 3.4l-.1.5L8 23.7v2.6l4.3 1.4.1.5c.3 1.2.8 2.3 1.4 3.4l.3.5-2 4 1.8 1.8 4-2 .5.3c1.1.6 2.2 1.1 3.4 1.4l.5.1 1.4 4.3z" />
      </svg>
      <!-- close icon -->
      <svg class="swap-on fill-current" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512">
        <polygon
          points="400 145.49 366.51 112 256 222.51 145.49 112 112 145.49 222.51 256 112 366.51 145.49 400 256 289.49 366.51 400 400 366.51 289.49 256 400 145.49" />
      </svg>

    </label>
    <ul class="dropdown-content bg-base-100/50 w-60 shadow
        p-2 rounded-box backdrop-blur-lg">
      <li class="text-sm font-bold text-gray-900">
        <span>Analyze option</span>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <input type="checkbox" class="toggle toggle-primary" checked>
            <span class="label-text text-gray-700">Whois</span>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <input type="checkbox" class="toggle toggle-primary" checked>
            <span class="label-text text-gray-700">GTmetrix</span>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <input type="checkbox" class="toggle toggle-primary" checked>
            <span class="label-text text-gray-700">Backlinks</span>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <input type="checkbox" class="toggle toggle-primary" checked>
            <span class="label-text text-gray-700">SSL</span>
          </label>
        </div>
      </li>
      <li>
        <div class="form-control">
          <label class="label cursor-pointer">
            <input type="checkbox" class="toggle toggle-primary" checked>
            <span class="label-text text-gray-700">AMP</span>
          </label>
        </div>
      </li>
    </ul>
  </div>
  <form class="flex flex-col items-center justify-center h-screen">

    <h1 class="text-4xl md:text-5xl xl:text-6xl font-black mb-3 md:mb-4 xl:mb-5 text-primary">Website Analyzer</h1>

    <input type="text" placeholder="exm: https://google.com/" class="input 
        input-bordered shadow-primary block shadow-sm input-primary w-3/6 xl:w-full max-w-xs input-md
        mb-3 md:mb-4 xl:mb-6">

    <button class="btn btn-primary text-center block">
      Analyze
    </button>

  </form>

  <div class="fixed w-52 h-52 md:w-72 md:h-72 xl:w-80 xl:h-80 bg-primary -bottom-24 -left-20 rounded-full"></div>

</template>

<script>
// @ is an alias to /src

export default {
  name: 'IndexPage',
  components: {
  },
  mounted() {
    const swapOptions = document.querySelector("#swap-options");
    console.log(swapOptions);

    swapOptions.addEventListener('toggle', () => {
      const dpContent = document.querySelector('.dropdown-content');
      dpContent.classList.add('visible');
      dpContent.classList.add('opacity-10');
    })
  },
}

</script>
