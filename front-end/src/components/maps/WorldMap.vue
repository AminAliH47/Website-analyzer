<template>
    <div :id="this.id" class="m-auto h-96 w-full xl:w-112"></div>
</template>

<script>
import jsVectorMap from 'jsvectormap'
import 'jsvectormap/dist/maps/world-merc'

export default {
    name: "WordMap",
    props: {
        id: {
            type: String,
            require: true,
        }
    },
    mounted() {
        const map = new jsVectorMap({
            selector: `#${this.id}`,
            map: 'world_merc',
            regionStyle: {
                initial: {
                    fill: '#5C7F67',
                    stroke: "#E9E7E7",
                    strokeWidth: 1.5,
                    fillOpacity: 1
                },
                hover: { fill: '#5D5656' },
                selected: { fill: '#f66' },
            },
            selectedRegions: ["IR"],
            zoomButtons: false,
            showTooltip: false,
        });
        map.addMarkers([
            {
                name: 'Iran',
                coords: [33, 52],
                style: { fill: '#5C7F67' }
            },
        ])
    },
}
</script>