<template>
    <div class="responsive-wrapper">
        <div class="responsive">
            <div class="desktop">
                <div class="trim">
                    <iframe src="https://mashadsanat.ir" frameborder="0" loading="lazy"></iframe>
                </div>
            </div>
            <div class="laptop">
                <div class="trim">
                    <iframe src="https://mashadsanat.ir" frameborder="0" loading="lazy"></iframe>
                </div>
            </div>
            <div class="phone">
                <div class="trim">
                    <iframe src="https://mashadsanat.ir" frameborder="0" loading="lazy"></iframe>
                </div>
            </div>
            <div class="tablet">
                <div class="trim">
                    <iframe src="https://mashadsanat.ir" frameborder="0" loading="lazy"></iframe>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ResponsiveComponent",
}
</script>

<style scoped>
iframe {
    transform: scale(0.219);
    transform-origin: left top;
    margin: 0px;
    padding: 0px;
    position: relative;
    background-color: rgb(255, 255, 255);
    border-color: rgb(0, 0, 0);
}
</style>