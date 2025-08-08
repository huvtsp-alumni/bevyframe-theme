css = """
      .background-img {
          background-image: url('/assets/img/background.jpeg');
          background-size: cover;
          background-position: center;
          background-color: #dde4ec;
      }

      .info-notification {
          background-image: linear-gradient(330deg, rgba(164, 214, 255, 0.4) 0%, rgba(190, 216, 236, 0.4) 100%);
      }

      .warning-notification {
          background-image: linear-gradient(330deg, rgba(255, 251, 181, 0.4) 0%, rgba(236, 232, 164, 0.4) 100%);
      }

      .error-notification {
          background-image: linear-gradient(330deg, rgba(255, 189, 181, 0.4) 0%, rgba(236, 172, 164, 0.4) 100%);
      }

      @media (prefers-color-scheme: dark) {
          .background-img {
              background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url('/assets/img/background.jpeg');
          }

          h1#greeting {
              color: #fff;
          }
      }

      #root {
          position: relative;
          width: 100%;
          max-width: 1500px;
          height: 100vh;
          margin: 0 auto !important;
          overflow: hidden;
          padding: 0 !important;
      }

      body {
          height: 100%;
          overflow: hidden;
          margin: 0;
          padding: 0;
      }
      """