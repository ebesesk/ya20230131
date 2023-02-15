<script>

  import fastapi from "../../lib/api";
  import { page, keyword } from "../../lib/store"
  import { clickOutside } from "../../lib/clickOutside";
  
  import Modal from "../../components/Modal.svelte";
  import VideoInfo from "./components/VideoInfo.svelte" 
  import ScanFiles from "./components/Scanfiles.svelte"
  import Search from "./components/Search.svelte";
  import Post from "./components/Post.svelte";
  
  let video_list = []
  let size = 16
  let total = 0
  let modal_scanfiles
  let modal_videoInfo
  let modal_search
  let modal_post
  let videoInfo   // modal_videoInfo props
  
  
  function open_videoInfo_modal(video) {
    videoInfo = video
    modal_videoInfo.show()
  }
  
  
  function search_video() {
    let params = {
      page: $page,
      size: size,
      keyword: $keyword
    }
    fastapi('get', '/api/video/search', params, (json) => {
      console.log(json.video_list)
      video_list = json.video_list
      total = json.total
    })
  }

  function voteVideo(_video_id) {
    let url = "/api/video/vote"
    let params = {
      video_id: _video_id
    }
    fastapi('post', url, params,
      (json) => {
        search_video()
      },
      (err_json) => {
        error = err_json
      }
    )
  }
  function delVote(_video_id) {
    let url = "/api/video/delvote"
    let params = {
      video_id: _video_id,
    }
    fastapi('delete', url, params,
      (json) => {
        search_video()
      },
      (err_json) => {
        error = err_json
      }
    )
  }

  $: total_page = Math.ceil(total/size)    
  $: $page, $keyword, search_video()
  
</script>







<div class="container-xxl my-2"  >

  <div class="header-button">
    <button class="button" on:click={modal_scanfiles.show()}>ScanFiles</button>
    <button class="button" on:click={modal_post.show()}>POST</button>
    <button class="button" on:click={modal_search.show()}>검색</button>
  </div>

  <!-- 페이징처리 시작 -->
  <ul class="pagination justify-content-center" style="font-size: smaller;">
    <!-- 이전페이지 -->
    <li class="page-item {$page <= 0 && 'disabled'}">
      <button class="page-link" on:click="{() => $page--}"  style="font-size: smaller;">이전</button>
    </li>
    <!-- 페이지번호 -->
    {#each Array(total_page) as _, loop_page}
    {#if loop_page >= $page-5 && loop_page <= $page+5}
          
    <!-- <li class="page-item {(loop_page === $page && videoinfo_modal) &&  'active'}"> -->
    <li class="page-item ">
      <button on:click="{() => $page = loop_page}" class="page-link {(loop_page === $page) && 'font-weight-bol text-danger'}"  style="font-size: smaller;">{loop_page+1}</button>
    </li>
    {/if}
    {/each}
    <!-- 다음페이지 -->
    <li class="page-item {$page >= total_page-1 && 'disabled'}">
      <button class="page-link" on:click="{() => $page++}"  style="font-size: smaller;">다음</button>
    </li>
    <li>
    </li>
  </ul>
  <!-- 페이징처리 끝 -->



  <div class="row" style="float: none; margin:100 auto;">
    {#each video_list as video}
    <div class="col-xxl-2 col-xl-3 col-lg-4 col-sm-6" style="object-fit: scale-down;">
      <div class="img-container" style="text-align: center;">
        <img 
          src='{
            encodeURIComponent("/video/" + 
            video.dbid.substring(0,video.dbid.indexOf('/')+1) + 
            'gif/' + video.dbid.substring(video.dbid.indexOf('/')+1, video.dbid.lastIndexOf('.')) + ".gif")  
          }' 
            alt="" class="img-thumbnail img-responsive">
          <br>
        <!-- 추천 -->
        {#if video.voter.length > 0}
          <button class="btn btn-sm btn-light" on:click="{delVote(video.id)}">
            <sapn class="badge rounded-pill bg-danger">{video.voter.length}</sapn>
          </button>
        {:else}
        <button class="btn btn-sm btn-light" on:click="{voteVideo(video.id)}">
          추천
        </button>
        {/if}

        <button class="btn btn-sm light" on:click={open_videoInfo_modal(video)}>modal</button>
        <a href="{'kddddds://http://' + video.dbid}" 
          class="caption display-7" 
          style="font-size:smaller; white-space: normal; word-break: break-all;">
              # {video.dbid.substr(0,20)} 
        </a>
        <sapn class="video-info">
          # {video.etc} # {video.width}x{video.height} 
          # {parseInt(video.showtime/60)}분{video.showtime%60}초
          # {parseInt(video.bitrate/1000)}kbps # {parseInt(video.filesize/1000000)}MB
          <!-- # 수정 날자: {video.date_modified}  # 작성 날자: {video.date_posted}  # cdate: {video.cdate}<br> -->
        </sapn>
      </div>
    </div>
    {/each}
  </div>
        


  <!-- 페이징처리 시작 -->
  <ul class="pagination justify-content-center" style="font-size: smaller;">
    <!-- 이전페이지 -->
    <li class="page-item {$page <= 0 && 'disabled'}">
      <button class="page-link" on:click="{() => $page--}"  style="font-size: smaller;">이전</button>
    </li>
    <!-- 페이지번호 -->
    {#each Array(total_page) as _, loop_page}
    {#if loop_page >= $page-5 && loop_page <= $page+5}
          
    <!-- <li class="page-item {(loop_page === $page && videoinfo_modal) &&  'active'}"> -->
    <li class="page-item ">
              
      <button on:click="{() => $page = loop_page}" class="page-link {(loop_page === $page) && 'font-weight-bol text-danger'}"  style="font-size: smaller;">{loop_page+1}</button>
    </li>
    {/if}
    {/each}
    <!-- 다음페이지 -->
    <li class="page-item {$page >= total_page-1 && 'disabled'}">
      <button class="page-link" on:click="{() => $page++}"  style="font-size: smaller;">다음</button>
    </li>
    <li>
    </li>
  </ul>
  <!-- 페이징처리 끝 -->
        
</div>



<!-- 모달 -->
<Modal bind:this={modal_videoInfo}>
<!-- Modal content -->
  <VideoInfo videoInfo={videoInfo}/>
  <button on:click={modal_videoInfo.hide()} style="font-size: smaller;">Close</button>
</Modal>

<Modal bind:this={modal_scanfiles}>
  <!-- Modal content -->
  <ScanFiles />
  <button on:click={modal_scanfiles.hide()} style="font-size: smaller;">Close</button>
</Modal>

<Modal bind:this={modal_search}>
  <!-- Modal content -->
  <Search />
  <button on:click={modal_search.hide()} style="font-size: smaller; text-align: right;">Close</button>
</Modal>

<Modal bind:this={modal_post}>
  <!-- Modal content -->
  <Post />
  <button on:click={modal_post.hide()} style="font-size: smaller; text-align: right;">Close</button>
</Modal>



<!-- 모달끝 -->


<style>
.caption.display-7 {
  font-size: smaller;
  line-height: 0px;
  text-decoration: none;
  color: black;
}
.img-thumbnail {
  height: 200px;
  text-align: center;
}
.header-button {
      display: flex;
      justify-content: flex-end;
      font-size: smaller;
      /* line-height: 100%; */
      align-items: center;

    }
.button-group {
  /* display: inline-flex; */
  text-align: end;
  /* border: 1px solid #cccccc; */
  border-radius: 4px;
  /* overflow: hidden; */
  font-size: smaller;
}

.button {
  font-size: smaller;
  padding: 10px 16px;
  outline: none;
  border: none;
  cursor: pointer;
  border-right: 1px solid #ffffff;
  background: #ffffff;
  /* font-family: "Inter", sans-serif; */
}

.button:last-child {
  border-right: none;
}

.button:hover {
  background: #cccccc;
}

.page-item {
  font-size: smaller;
}
.img-thumbnail.img-responsive {
  object-fit: scale-down;
}
.video-info {
  font-size: smaller;
  line-height: 1;
}
a {
  line-height: 1;
}
.btn-sm.btn-light {
  font-size: smaller;
}
.badge {
  font-size: smaller;
}

</style>