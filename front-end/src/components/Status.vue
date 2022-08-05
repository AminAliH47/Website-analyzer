<template>
    <div class="stats stats-vertical md:stats-horizontal shadow-lg">

        <div class="stat bg-base-100 z-10">
            <div class="stat-figure">
                <a href="#" class="btn btn-ghost text-primary">
                    <LightningBoltIcon class="h-10 w-10 text-success" />
                </a>
            </div>
            <div class="stat-title">GTmetrix Status</div>
            <div class="text-primary h-28">
                <div class="radial-progress bg-white text-success 
                my-3 border-4 border-white" style="--value:70; ----thickness: 15px;">
                    86%
                </div>
            </div>

            <div class="stat-desc">
                <a href="#" class="btn btn-link text-success gap-2 normal-case p-0">
                    Read more
                    <ChevronDoubleDownIcon class="h-5 w-5" />
                </a>
            </div>
        </div>

        <div class="stat bg-base-100 z-10">
            <div class="stat-figure text-primary">
                <EyeIcon class="h-10 w-10" />
            </div>
            <div class="stat-title">Page Views</div>
            <div class="text-primary h-28 flex items-center justify-start">
                <h2 class="text-4xl font-black">
                    2k
                </h2>
            </div>
            <div class="stat-desc">
                <a href="#" class="btn btn-link text-primary gap-2 normal-case p-0">
                    Read more
                    <ChevronDoubleDownIcon class="w-5 h-5" />
                </a>
            </div>
        </div>

        <div class="stat bg-base-100 z-10">
            <div class="stat-figure text-primary">
                <LightningBoltIcon class="w-10 h-10" />
            </div>
            <div class="stat-title">Performance</div>
            <div class="text-primary h-28 flex items-center justify-start">
                <h2 class="text-4xl font-black">
                    30%
                </h2>
            </div>
            <div class="stat-desc">21% more than last month</div>
        </div>

        <div class="stat bg-base-100 z-10">
            <div class="stat-figure">
                <a href="#" class="btn btn-ghost text-primary">
                    <LightningBoltIcon class="h-10 w-10 text-error" />
                </a>
            </div>
            <div class="stat-title">Page speed</div>
            <div class="text-primary h-28">
                <div class="radial-progress bg-white text-error 
                my-3 border-4 border-white" style="--value:30; ----thickness: 15px;">
                    30%
                </div>
            </div>

            <div class="stat-desc">
                <a href="#" class="btn btn-link text-error font-bold gap-2 normal-case p-0">
                    Read more
                    <ChevronDoubleDownIcon class="h-5 w-5" />
                </a>
            </div>
        </div>

        <div class="stat bg-base-100 z-10">
            <div class="stat-figure">
                <a href="#" class="btn btn-ghost text-primary">
                    <LightningBoltIcon class="h-10 w-10 text-success" />
                </a>
            </div>
            <div class="stat-title">GTmetrix Status</div>
            <div class="text-primary h-28">
                <div class="radial-progress bg-white text-success 
                my-3 border-4 border-white" style="--value:70; ----thickness: 15px;">
                    86%
                </div>
            </div>

            <div class="stat-desc">
                <a href="#" class="btn btn-link text-success gap-2 normal-case p-0">
                    Read more
                    <ChevronDoubleDownIcon class="h-5 w-5" />
                </a>
            </div>
        </div>

    </div>
</template>

<script>
import { ChevronDoubleDownIcon, EyeIcon, LightningBoltIcon } from '@heroicons/vue/outline'

export default {
    name: "StatusComponent",
    components: {
        ChevronDoubleDownIcon,
        EyeIcon,
        LightningBoltIcon,
    }
}
</script>