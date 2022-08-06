<template>
    <div class="card w-full bg-base-100 shadow-xl  border border-primary/20">
        <div class="card-body items-start text-left">
            <h2 class="card-title">{{ title }}</h2>
            <p>{{ desc }}</p>
            <!-- <div class="card-actions">
                <button class="btn btn-primary">Buy Now</button>
            </div> -->
        </div>
        <div class="px-5 pt-5">
            <slot name="chart"></slot>
        </div>
    </div>
</template>

<script>
// import LineChart from './charts/LineChart.vue'

export default {
    name: "CardComponents",
    props: {
        title: {
            type: String,
            default: "Analyzer",
        },
        desc: {
            type: String,
            default: "This is Analyze",
        }
    }
}
</script>