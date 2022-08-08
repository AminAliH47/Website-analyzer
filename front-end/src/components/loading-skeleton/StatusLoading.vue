<template>
    <div class="stat bg-base-100 z-10 animate-pulse">
        <div class="stat-figure text-primary">
            <div class="w-12 bg-gray-300 h-12 rounded-full ">
            </div>
        </div>
        <div class="stat-title">
            <div class="w-28 bg-gray-300 h-3 rounded-md ">
            </div>
        </div>
        <div class="text-primary h-28 flex items-center justify-start">
            <h2 class="text-4xl font-black">
                <div class="w-20 bg-gray-300 h-10 rounded-md ">
                </div>
            </h2>
        </div>
        <div class="stat-desc">
            <div class="w-32 bg-gray-300 h-3 rounded-md ">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "StatusLoadingSkeleton",
}
</script>