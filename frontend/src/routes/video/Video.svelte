<script>
    import fastapi from "../../lib/api";
  //   import { link } from 'svelte-spa-router'
    import { page } from "../../lib/store"
    
    let search = "test2"
    let video_list = []
    let size = 18
    // let page = 0
    let total = 0
    $: total_page = Math.ceil(total/size)    
    
    console.log(import.meta.env.VITE_VIDEO_DIR)
    
    function get_videos_list(_page) {
        let params = {
            page: _page,
            size: size,
            search: search 
        }
        fastapi('get', '/api/video/list', params, (json) => {
            // console.log(json)
            video_list = json.video_list
            total = json.total
            $page = _page
        })
    }
    
    get_videos_list(0)
    
    import Modal from "../../components/Modal.svelte";
    import VideoInfo from "./components/VideoInfo.svelte" 
    import ScanFiles from "./components/Scanfiles.svelte"
    
    let modal_scanfiles
    let modal_videoInfo
    let video_id

    function open_videoInfo_modal(video) {
        video_id = video.id
        modal_videoInfo.show()
    }
    
    
</script>








<div class="container my-2 " style="width: 100%; height: 100%; ">
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center" style="font-size: smaller;">
        <!-- 이전페이지 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_videos_list($page-1)}"  style="font-size: smaller;">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
        {#if loop_page >= $page-5 && loop_page <= $page+5}
        <li class="page-item {loop_page === $page && 'active'}">
            <button on:click="{() => get_videos_list(loop_page)}" class="page-link"  style="font-size: smaller;">{loop_page+1}</button>
        </li>
        {/if}
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {$page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_videos_list($page+1)}"  style="font-size: smaller;">다음</button>
        </li>
        <button class="btn btn-sm justify-content-center" on:click={modal_scanfiles.show()}>Scan Files</button>
    </ul>
    <!-- 페이징처리 끝 -->
    
    <!-- <br><br><br><br><br><br><br><br><br><br><br><br><br><br> -->


    <div class="row" style="float: none; margin:100 auto;">
        {#each video_list as video}
        <div class="col-xxl-3 col-xl-4 col-lg-4 col-sm-6" style="object-fit: scale-down;">
            <div class="img-container">
                <img 
                src='{
                    encodeURIComponent("/video/" + 
                    video.dbid.substring(0,video.dbid.indexOf('/')+1) + 
                    'gif/' + video.dbid.substring(video.dbid.indexOf('/')+1, video.dbid.lastIndexOf('.')) + ".gif")  
                }' 
                    alt="" class="img-thumbnail img-responsive" 
                    style="object-fit: scale-down;">
                
                <button class="btn btn-sm" on:click={open_videoInfo_modal(video)}>modal</button>
                <a href="{'kddddds://http://' + video.dbid}" 
                    class="caption display-7" 
                    style="font-size:smaller; white-space: normal; word-break: break-all;">
                    {video.dbid.substring(video.dbid.indexOf('/')+1, video.dbid.lastIndexOf('.')).substr(0,16)}
                </a>
            </div>
        </div>
        {/each}
    </div>
        


    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <button class="page-link" on:click="{() => get_videos_list($page-1)}"  style="font-size: smaller;">이전</button>
        </li>
        <!-- 페이지번호 -->
        {#each Array(total_page) as _, loop_page}
        {#if loop_page >= $page-5 && loop_page <= $page+5}
        <li class="page-item {loop_page === $page && 'active'}">
            <button on:click="{() => get_videos_list(loop_page)}" class="page-link"  style="font-size: smaller;">{loop_page+1}</button>
        </li>
        {/if}
        {/each}
        <!-- 다음페이지 -->
        <li class="page-item {$page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{() => get_videos_list($page+1)}"  style="font-size: smaller;">다음</button>
        </li>
    </ul>
    <!-- 페이징처리 끝 -->
        
</div>


<!-- 모달 -->
<Modal bind:this={modal_videoInfo}>
<!-- Modal content -->
    <VideoInfo  video_id = {video_id}/>
    <button on:click={modal_videoInfo.hide()} style="font-size: smaller;">Close</button>
</Modal>

<Modal bind:this={modal_scanfiles}>
    <!-- Modal content -->
    <ScanFiles />
    <button on:click={modal_scanfiles.hide()} style="font-size: smaller;">Close</button>
</Modal>
    


<!-- 모달끝 -->
