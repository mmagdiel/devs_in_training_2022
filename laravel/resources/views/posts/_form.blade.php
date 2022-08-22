@csrf
<label class="uppercase text-gray-700 text-xs">Title</label>
<span class="text-xs text-red-600">@error('title') {{ $message }} @enderror</span>
<input type="text" name="title" class="rounded border-gray-200 w-full mb-4" value="{{ old('title', $post->title) }}" />

<label class="uppercase text-gray-700 text-xs">Slug</label>
<span class="text-xs text-red-600">@error('slug') {{ $message }} @enderror</span>
<input type="text" name="slug" class="rounded border-gray-200 w-full mb-4" value="{{ old('slug', $post->slug) }}" />

<label class="uppercase text-gray-700 text-xs">Title</label>
<span class="text-xs text-red-600">@error('body') {{ $message }} @enderror</span>
<textarea rows="3" name="body" class="rounded border-gray-200 w-full mb-4" >
    {{ old('body', $post->body) }}
</textarea>

<div class="flex justify-between items-center">
    <a href="{{ route('posts.index') }}" class="text-indigo-600">Back</a>
    <input type="submit" value="Save"  class="bg-gray-800 text-white rounded px-2 py-1" />
</div>