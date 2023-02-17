<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"
    import { access_token, username, is_login} from "../lib/store"

    let error = {detail:[]}
    let login_username = ""
    let login_password = ""

    function login(event) {
        event.preventDefault()
        let url = "/api/login"
        let params = {
            username: login_username,
            password: login_password,
        }
        fastapi ('login', url, params,
            (json) => {
                $access_token = json.access_token
                $username = json.username
                $is_login = true
                push("/home")
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>


<!--  html 전체 영역을 지정하는 container -->
<div id="container">
    <!--  login 폼 영역을 : loginBox -->
    <div id="loginBox">
    
      <!-- 로그인 페이지 타이틀 -->
      <div id="loginBoxTitle">LOGIN</div>
      <!-- 아이디, 비번, 버튼 박스 -->
      <div id="inputBox">
        <div class="input-form-box"><span>아이디 </span><input type="text" name="uid" class="form-control"></div>
        <div class="input-form-box"><span>비밀번호 </span><input type="password" name="upw" class="form-control"></div>
        <div class="button-login-box" >
          <button type="button" class="btn btn-primary btn-xs" style="width:100%">로그인</button>
        </div>
      </div>
      
    </div>
  </div>