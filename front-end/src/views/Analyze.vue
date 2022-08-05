<template>
    <!-- Shape 1 -->
    <div class="fixed w-44 h-44 xl:w-50 xl:h-50 bg-primary -left-20 top-28
   xl:top-24 xl:-left-20  rounded-full z-0"></div>
    <!-- Shape 2 -->
    <div class="fixed w-44 h-44 xl:w-56 xl:h-56 bg-primary -right-20 top-28
   xl:top-60 xl:-right-16 rounded-full z-0"></div>
    <Navbar />
    <div class=" w-11-5/12 mx-auto mt-10 flex flex-col justify-center">
        <Status />
        <div class="grid grid-cols-2 gap-4 mt-10">
            <div class="row-span-1">
                <Review />
            </div>
            <div class="row-span-1">
                <Review />
            </div>
        </div>
    </div>
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue"
import StatusComponent from "@/components/Status.vue"
import ReviewComponent from "@/components/Review.vue"

export default {
    name: 'AnalyzePage',
    components: {
        'Navbar': NavbarComponent,
        'Status': StatusComponent,
        'Review': ReviewComponent,
    },
}
</script>