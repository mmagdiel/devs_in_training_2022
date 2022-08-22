<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            {{ __('Show') }}
        </h2>
    </x-slot>

    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg">
                <div class="p-6 bg-white border-b border-gray-200">
                    <div class="flex justify-between align-center my-4">
                        <h4 class="text-xl">Post details</h4>
                        <a href="{{ route('posts.index') }}" class="bg-gray-800 text-white rounded px-2 py-1">Back</a>
                    </div>
                    <dl class="my-2">
                        <dt class="text-lg inline">
                            Title:                           
                        </dt>
                        <dd class="inline text-gray-700">
                            {{ $post->title }}
                        </dd>
                    </dl>
                    <dl class="my-2">
                        <dt class="text-lg inline">
                            Slug: 
                        </dt>
                        <dd class="inline text-gray-700">
                            {{ $post->slug }}
                        </dd>
                    </dl>
                    <dl class="my-2">
                        <dt class="text-lg inline">
                            Username:
                        </dt>
                        <dd class="inline text-gray-700">
                            {{ $post->user->name }}
                        </dd>
                    </dl>
                    <dl class="my-2">
                        <dt class="text-lg inline">
                            Body: 
                        </dt>
                        <dd class="inline text-gray-700">
                            {{ $post->body }}
                        </dd>
                    </dl>
                </div>
            </div>
        </div>
    </div>
</x-app-layout>
