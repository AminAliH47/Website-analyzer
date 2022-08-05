<template>
    <div class="card w-full bg-base-100 shadow-xl">
        <div class="px-5 pt-5">
            <Line :height=200 />
        </div>
        <div class="card-body items-center text-center">
            <h2 class="card-title">Shoes!</h2>
            <p>If a dog chews shoes whose shoes does he choose?</p>
            <div class="card-actions">
                <button class="btn btn-primary">Buy Now</button>
            </div>
        </div>
    </div>
</template>

<script>
import LineChart from './charts/LineChart.vue'

export default {
    name: "ReviewComponents",
    components: {
        "Line": LineChart,
    },
}
</script>