<template>
    <Line :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId" :dataset-id-key="datasetIdKey"
        :plugins="plugins" :css-classes="cssClasses" :styles="styles" :width="width" :height="height" />
</template>

<script>
import { Line } from 'vue-chartjs'
import {
    Chart as ChartJS,
    ArcElement,
    LineElement,
    BarElement,
    PointElement,
    BarController,
    BubbleController,
    DoughnutController,
    LineController,
    PieController,
    PolarAreaController,
    RadarController,
    ScatterController,
    CategoryScale,
    LinearScale,
    LogarithmicScale,
    RadialLinearScale,
    TimeScale,
    TimeSeriesScale,
    Decimation,
    Filler,
    Legend,
    Title,
    Tooltip,
    SubTitle
} from 'chart.js'

ChartJS.register(
    ArcElement,
    LineElement,
    BarElement,
    PointElement,
    BarController,
    BubbleController,
    DoughnutController,
    LineController,
    PieController,
    PolarAreaController,
    RadarController,
    ScatterController,
    CategoryScale,
    LinearScale,
    LogarithmicScale,
    RadialLinearScale,
    TimeScale,
    TimeSeriesScale,
    Decimation,
    Filler,
    Legend,
    Title,
    Tooltip,
    SubTitle
)

export default {
    name: 'LineChart',
    components: {
        Line,
    },
    props: {
        chartId: {
            type: String,
            default: 'line-chart'
        },
        datasetIdKey: {
            type: String,
            default: 'label'
        },
        width: {
            type: Number,
            default: 400
        },
        height: {
            type: Number,
            default: 400,
        },
        cssClasses: {
            default: '',
            type: String
        },
        styles: {
            type: Object,
            default: () => { }
        },
        plugins: {
            type: Array,
            default: () => []
        },
        data: {
            type: Array,
            default: () => [],
        }
    },
    data() {
        return {
            chartData:
            {
                labels: this.data,
                datasets: [
                    {
                        label: "Number of Moons",
                        data: [0, 124, 50, 230],
                        backgroundColor: "rgba(54,73,93,.5)",
                        borderColor: "#36495d",
                        borderWidth: 3
                    },
                    {
                        label: "Planetary Mass (relative to the Sun x 10^-6)",
                        data: [200, 400, 140, 300],
                        backgroundColor: "rgba(71, 183,132,.5)",
                        borderColor: "#47b784",
                        borderWidth: 3
                    }
                ],
            },

            chartOptions: {
                responsive: true
            }
        }
    }
}
</script>