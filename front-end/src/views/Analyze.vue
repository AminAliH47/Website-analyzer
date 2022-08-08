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
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-6 lg:mt-10">
            <div class="row-span-1">
                <Card title="Hello" desc="This is a test text">
                    <template v-slot:chart>
                        <Line :height=200 :data="['Hello', 'test', 'test', 'Worlds']" />
                    </template>
                </Card>
            </div>
            <div class="row-span-1">
                <Card>
                    <template v-slot:chart>
                        <Line :height=200 :data="['Hello', 'test', 'test', 'Worlds']" />
                    </template>
                </Card>
            </div>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 mt-6 lg:mt-10">
            <div class="row-span-1">
                <Card title="Your Website IP Location" desc="Iran - Tehran">
                    <template v-slot:chart>
                        <WorldMap id="world-map" />
                    </template>
                </Card>
            </div>
            <div class="row-span-1">
                <Card title="About your website"
                    desc="In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may b">
                </Card>
            </div>
        </div>

        <div class="grid grid-cols-1 gap-4 mt-6 lg:mt-10">
            <div class="row-span-1">
                <Card title="Is Your Website Responsive?" desc="" id="responsive">
                    <template v-slot:chart>
                        <Responsive />
                    </template>
                </Card>
            </div>
        </div>
    </div>
    <Footer />
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue"
import StatusComponent from "@/components/Status.vue"
import CardComponent from "@/components/Card.vue"
import LineChart from '@/components/charts/LineChart.vue'
import WorldMap from '@/components/maps/WorldMap.vue'
import ResponsiveComponent from '@/components/Responsive.vue'
import FooterComponent from '@/components/Footer.vue'

export default {
    name: 'AnalyzePage',
    components: {
        'Navbar': NavbarComponent,
        'Status': StatusComponent,
        'Card': CardComponent,
        'Line': LineChart,
        WorldMap,
        "Responsive": ResponsiveComponent,
        "Footer": FooterComponent,
    },
}
</script>

<style>
body {
    overflow-x: hidden;
    overflow-y: scroll;
}
</style>