<script>
    import fastapi from "../../lib/api";
  //   import { link } from 'svelte-spa-router'
    import { page } from "../../lib/store"
    
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
    import VideoInfo from "./VideoInfo.svelte" 
    let modal
    let videoInfo
    function open_videoInfo_modal(video) {
        videoInfo = video
        modal.show()
    }
</script>





<div class="container my-2 " style="width: 100%; height: 100%; ">
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

                <!-- 모달 -->
                <button class="btn btn-sm" on:click={open_videoInfo_modal(video)}>modal</button>
                <Modal bind:this={modal}>
                <!-- Modal content -->
                    <VideoInfo  videoInfo = {videoInfo}/>
                    <button on:click={modal.hide()}>Close</button>
                </Modal>
                <!-- 모달끝 -->

                <a href="{'kddddds://http://' + video.dbid}" 
                    class="caption display-7" 
                    style="font-size:smaller; white-space: normal; word-break: break-all;">
                    {video.dbid.substring(video.dbid.indexOf('/')+1, video.dbid.lastIndexOf('.')).substr(0,16)}
                </a>
                <p>{video.id}</p>
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
    
    

